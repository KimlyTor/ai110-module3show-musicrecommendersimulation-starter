# 🎵 Music Recommender Simulation

## Project Summary
<!--
In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does. 
-->
This project recommends songs based on a listener's music preferences. It compares each song's genre, mood, and energy with the listener's choices, then ranks the songs by how closely they match. The goal is to explore how a simple recommendation system can use song features to help people discover music they may enjoy.

---

## How The System Works
<!--
Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
-->

Each song has a genre, mood, energy level, and acousticness value, along with its title and artist. The user picks the kind of music they like, the mood they want, and an energy level. They can also say whether they want more acoustic songs, less acoustic songs, or have no preference. The recommender compares each song with those choices and gives it a score. If the user has no acoustic preference, that feature is left out. Finally, it shows the songs with the highest scores first.

```text
INPUT: User Preferences
favorite genre, favorite mood, target energy,
and acoustic preference
          │
          ▼
PROCESS: Score every song in songs.csv
For each song:
  • Compare its genre with the favorite genre
  • Compare its mood with the favorite mood
  • Score how close its energy is to the target energy
  • If the user has an acoustic preference, score that too
          │
          ▼
RANKING: Sort songs by score, highest first
          │
          ▼
OUTPUT: Top K Recommendations
Return the first K songs, with their scores
```

### How Recommendations Are Scored

The recommender scores each song out of 100. First, it calculates a match value for each feature:

- **Genre match (G):** `1` if the song's genre matches the user's favorite genre; otherwise `0`.
- **Mood match (M):** `1` if the song's mood matches the user's favorite mood; otherwise `0`.
- **Energy match (E):** `1 - abs(song energy - target energy)`. Both energy values are between `0` and `1`, so a closer match gets a higher value.
- **Acousticness match (A), when requested:** use the song's acousticness value for “prefer acoustic,” or `1 - song acousticness` for “prefer less acoustic.” Both are between `0` and `1`.

If the user has no acousticness preference:

```text
Score = (40 × G) + (30 × M) + (30 × E)
```

If the user prefers acoustic or less-acoustic songs:

```text
Score = (35 × G) + (25 × M) + (25 × E) + (15 × A)
```

The weights add up to 100 in each version. For example, if genre and mood match (`G = 1`, `M = 1`) and the song's energy is `0.82` while the user's target is `0.80`, then `E = 1 - abs(0.82 - 0.80) = 0.98`. With no acousticness preference, the score is `(40 × 1) + (30 × 1) + (30 × 0.98) = 99.4`.

Potential bias: Genre has the largest weight, so a song in the user's favorite genre may rank above a song that better matches their mood and energy. Exact genre labels can also hide similarities between related genres.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output
<!--
Paste a sample of your recommender's output here as a text block so a reader can see what it produces:
-->
```
User profile:
- Favorite genre: pop
- Favorite mood: happy
- Target energy: 0.80
- Acoustic preference: no preference

Top 5 recommendations:

Sunrise City - Score: 99.40/100
Because:
- Genre match (+40.0 points).
- Mood match (+30.0 points).
- Energy closeness (0.98) (+29.4 points).

Gym Hero - Score: 66.10/100
Because:
- Genre match (+40.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.87) (+26.1 points).

Rooftop Lights - Score: 58.80/100
Because:
- Genre does not match (+0.0 points).
- Mood match (+30.0 points).
- Energy closeness (0.96) (+28.8 points).

Golden Hour Groove - Score: 29.10/100
Because:
- Genre does not match (+0.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.97) (+29.1 points).

Night Drive Loop - Score: 28.50/100
Because:
- Genre does not match (+0.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.95) (+28.5 points).
```
```
Selected profile: Conflicting mood and energy: rock, sad, energy 0.95

User profile:
- Favorite genre: rock
- Favorite mood: sad
- Target energy: 0.95
- Acoustic preference: no preference

Top 5 recommendations:

Storm Runner - Score: 68.80/100
Because:
- Genre match (+40.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.96) (+28.8 points).

Iron Horizon - Score: 29.70/100
Because:
- Genre does not match (+0.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.99) (+29.7 points).

Gym Hero - Score: 29.40/100
Because:
- Genre does not match (+0.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.98) (+29.4 points).

Mirrorball Mystery - Score: 27.90/100
Because:
- Genre does not match (+0.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.93) (+27.9 points).

Golden Hour Groove - Score: 26.40/100
Because:
- Genre does not match (+0.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.88) (+26.4 points).
```
```
Selected profile: Genre versus mood and energy: pop, chill, energy 0.42

User profile:
- Favorite genre: pop
- Favorite mood: chill
- Target energy: 0.42
- Acoustic preference: no preference

Top 5 recommendations:

Midnight Coding - Score: 60.00/100
Because:
- Genre does not match (+0.0 points).
- Mood match (+30.0 points).
- Energy closeness (1.00) (+30.0 points).

Sunrise City - Score: 58.00/100
Because:
- Genre match (+40.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.60) (+18.0 points).

Library Rain - Score: 57.90/100
Because:
- Genre does not match (+0.0 points).
- Mood match (+30.0 points).
- Energy closeness (0.93) (+27.9 points).

Spacewalk Thoughts - Score: 55.80/100
Because:
- Genre does not match (+0.0 points).
- Mood match (+30.0 points).
- Energy closeness (0.86) (+25.8 points).

Gym Hero - Score: 54.70/100
Because:
- Genre match (+40.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.49) (+14.7 points).
```
```
Selected profile: Acoustic preference versus high energy: pop, happy, energy 0.95

User profile:
- Favorite genre: pop
- Favorite mood: happy
- Target energy: 0.95
- Acoustic preference: prefer acoustic

Top 5 recommendations:

Sunrise City - Score: 84.45/100
Because:
- Genre match (+35.0 points).
- Mood match (+25.0 points).
- Energy closeness (0.87) (+21.8 points).
- Acousticness match (0.18) (+2.7 points).

Gym Hero - Score: 60.25/100
Because:
- Genre match (+35.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.98) (+24.5 points).
- Acousticness match (0.05) (+0.8 points).

Rooftop Lights - Score: 50.50/100
Because:
- Genre does not match (+0.0 points).
- Mood match (+25.0 points).
- Energy closeness (0.81) (+20.2 points).
- Acousticness match (0.35) (+5.2 points).

Storm Runner - Score: 25.50/100
Because:
- Genre does not match (+0.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.96) (+24.0 points).
- Acousticness match (0.10) (+1.5 points).

Iron Horizon - Score: 25.20/100
Because:
- Genre does not match (+0.0 points).
- Mood does not match (+0.0 points).
- Energy closeness (0.99) (+24.8 points).
- Acousticness match (0.03) (+0.4 points).
```
**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---


## Experiments You Tried
<!--
Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users
-->

I tested four profiles. The original, used as the baseline for comparisons, is pop/happy with energy `0.80` and no acoustic preference; the other profiles are rock/sad with energy `0.95`, pop/chill with energy `0.42`, and pop/happy with energy `0.95` plus a preference for acoustic music. In the weight-shift experiment, I halved genre's weight and doubled energy's weight. The scores changed; the baseline and rock/sad profiles kept the same top-five songs, while the pop/chill list replaced “Sunrise City” and “Gym Hero” with “Focus Flow” and “Blue Lanterns.” The acoustic profile kept the same five songs but changed their order. I was surprised that pop/chill's top pick was lofi rather than pop, because its exact mood and energy match outweighed genre.

| Profile pair | What changed | Why it makes sense |
|---|---|---|
| Original vs. rock/sad | They share “Gym Hero” and “Golden Hour Groove”; rock/sad includes “Storm Runner” and “Iron Horizon.” | The rock profile rewards rock genre and high energy. No song in the catalog has a sad mood label. |
| Original vs. pop/chill | The top-five lists have no songs in common; pop/chill includes “Midnight Coding” and “Library Rain.” | Those songs match the chill mood and low energy target, even though they are not pop. |
| Original vs. pop/happy/acoustic | They share “Sunrise City,” “Rooftop Lights,” and “Gym Hero”; the remaining songs differ. | The higher energy target and acoustic preference shift scores and rankings. |
| Rock/sad vs. pop/chill | The top-five lists have no songs in common. | Rock/sad favors high energy, while pop/chill favors a chill mood and lower energy. |
| Rock/sad vs. pop/happy/acoustic | They share “Gym Hero,” “Iron Horizon,” and “Storm Runner”; pop/happy/acoustic also includes “Sunrise City” and “Rooftop Lights.” | The shared songs are high-energy; the latter profile additionally rewards pop genre and happy mood. |
| Pop/chill vs. pop/happy/acoustic | The top-five lists have no songs in common. | Their mood and energy preferences differ, and only pop/happy/acoustic applies an acousticness preference. |

The recommendations changed in response to the preferences and weight shift, but I cannot say they became more accurate without feedback from listeners.


---

## Limitations and Risks
<!--
Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.
-->

The catalog is small, with 20 songs across 17 genres, so many genres have only one example. The recommender requires exact genre and mood matches, treating related labels like “pop” and “indie pop” as different. This can limit variety and miss songs a listener might enjoy, especially when their preferences are not well represented in the catalog.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

<!--
Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
-->
