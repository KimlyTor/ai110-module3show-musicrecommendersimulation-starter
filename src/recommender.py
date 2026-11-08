from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    # TODO: Implement CSV loading logic
    # print(f"Loading songs from {csv_path}...")
    # return []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        songs = list(csv.DictReader(csv_file))

    for song in songs:
        song["id"] = int(song["id"])
        song["energy"] = float(song["energy"])
        song["tempo_bpm"] = int(song["tempo_bpm"])
        song["valence"] = float(song["valence"])
        song["danceability"] = float(song["danceability"])
        song["acousticness"] = float(song["acousticness"])

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences and return reasons."""
    # TODO: Implement scoring logic using your Algorithm Recipe from Phase 2.
    # Expected return format: (score, reasons)
    # return []
    acoustic_preference = user_prefs.get(
        "acoustic_preference", "no preference"
    ).strip().casefold()
    if acoustic_preference not in (
        "prefer acoustic",
        "prefer less acoustic",
        "no preference",
    ):
        raise ValueError(
            "acoustic_preference must be 'prefer acoustic', "
            "'prefer less acoustic', or 'no preference'."
        )

    # Experimental shift: halve genre weight and double energy weight.
    if acoustic_preference == "no preference":
        genre_weight, mood_weight, energy_weight = 20, 30, 60
    else:
        genre_weight, mood_weight, energy_weight = 17.5, 25, 50

    genre_match = (
        song["genre"].strip().casefold()
        == user_prefs["genre"].strip().casefold()
    )
    mood_match = (
        song["mood"].strip().casefold()
        == user_prefs["mood"].strip().casefold()
    )
    energy_match = 1 - abs(float(song["energy"]) - float(user_prefs["energy"]))

    genre_points = genre_weight * genre_match
    mood_points = mood_weight * mood_match
    energy_points = energy_weight * energy_match
    score = genre_points + mood_points + energy_points
    reasons = [
        f"Genre {'match' if genre_match else 'does not match'} "
        f"(+{genre_points:.1f} points).",
        f"Mood {'match' if mood_match else 'does not match'} "
        f"(+{mood_points:.1f} points).",
        f"Energy closeness ({energy_match:.2f}) "
        f"(+{energy_points:.1f} points).",
    ]

    if acoustic_preference != "no preference":
        acousticness = float(song["acousticness"])
        acoustic_match = (
            acousticness
            if acoustic_preference == "prefer acoustic"
            else 1 - acousticness
        )
        acoustic_points = 15 * acoustic_match
        score += acoustic_points
        reasons.append(
            f"Acousticness match ({acoustic_match:.2f}) "
            f"(+{acoustic_points:.1f} points)."
        )

    return score, reasons
    

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs ranked by score with explanations."""
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    #return []
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "\n".join(f"- {reason}" for reason in reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda result: result[1], reverse=True)
    return scored_songs[:max(0, k)]
