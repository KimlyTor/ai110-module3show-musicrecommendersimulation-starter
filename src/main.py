"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    # print(f"Loaded songs: {len(songs)}")
    

    profiles = [
        (
            "Original: pop, happy, energy 0.8",
            {"genre": "pop", "mood": "happy", "energy": 0.8},
        ),
        (
            "Conflicting mood and energy: rock, sad, energy 0.95",
            {"genre": "rock", "mood": "sad", "energy": 0.95},
        ),
        (
            "Genre versus mood and energy: pop, chill, energy 0.42",
            {"genre": "pop", "mood": "chill", "energy": 0.42},
        ),
        (
            "Acoustic preference versus high energy: pop, happy, energy 0.95",
            {
                "genre": "pop",
                "mood": "happy",
                "energy": 0.95,
                "acoustic_preference": "prefer acoustic",
            },
        ),
    ]

    print("\nChoose a user profile:")
    for index, (description, _) in enumerate(profiles, start=1):
        print(f"{index}. {description}")

    while True:
        selection = input(f"Enter a number (1-{len(profiles)}): ").strip()
        if selection.isdigit() and 1 <= int(selection) <= len(profiles):
            break
        print(f"Please enter a number from 1 to {len(profiles)}.")

    profile_name, user_prefs = profiles[int(selection) - 1]
    print(f"\nSelected profile: {profile_name}")

    print("\nUser profile:")
    print(f"- Favorite genre: {user_prefs['genre']}")
    print(f"- Favorite mood: {user_prefs['mood']}")
    print(f"- Target energy: {user_prefs['energy']:.2f}")
    print(
        "- Acoustic preference: "
        f"{user_prefs.get('acoustic_preference', 'no preference')}"
    )

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\nTop {len(recommendations)} recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f} points")
        print("Because:")
        print(explanation)
        print()


if __name__ == "__main__":
    main()
