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
    

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

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
        print(f"{song['title']} - Score: {score:.2f}/100")
        print("Because:")
        print(explanation)
        print()


if __name__ == "__main__":
    main()
