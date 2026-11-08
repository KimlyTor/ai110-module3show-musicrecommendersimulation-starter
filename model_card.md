# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

<!--
Give your model a short, descriptive name.
Example: **VibeFinder 1.0**
-->

**SongsMatcher 1.0**

---

## 2. Intended Use

<!--
Describe what your recommender is designed to do and who it is for.

Prompts:

- What kind of recommendations does it generate
- What assumptions does it make about the user
- Is this for real users or classroom exploration
-->

SongsMatcher 1.0 helps pick songs from a small list. It looks at the genre and mood the listener likes, and how much energy they want. The listener can also choose acoustic music, less-acoustic music, or no preference. 

---

## 3. How the Model Works

<!--
Explain your scoring approach in simple language.

Prompts:

- What features of each song are used (genre, energy, mood, etc.)
- What user preferences are considered
- How does the model turn those into a score
- What changes did you make from the starter logic

Avoid code here. Pretend you are explaining the idea to a friend who does not program.
-->

SongsMatcher 1.0 looks at one song at a time. It checks whether the song's genre and mood match what the listener picked, and whether the song's energy is close to the energy they want. If they chose an acoustic preference, it checks that too.

Each song gets up to 100 points. When the listener has no acoustic preference, genre is worth 40 points, mood 30, and energy 30. When they do have an acoustic preference, genre, mood, and energy are worth 35, 25, and 25 points, and acousticness is worth 15. Songs with the most points are shown first, with a short explanation of the points.

The starter code did not yet score or rank songs in the command-line demo. I added the point rules, explanations, and sorting so the demo can show the highest-scoring songs first.

---

## 4. Data

<!--
Describe the dataset the model uses.

Prompts:

- How many songs are in the catalog
- What genres or moods are represented
- Did you add or remove data
- Are there parts of musical taste missing in the dataset
-->

The CSV file has 20 sample songs. They cover 17 genres, including pop, rock, jazz, country, hip-hop, and blues, and 16 moods, including happy, chill, focused, playful, and peaceful.

The starter file had 10 songs, and 10 example songs were added. The added song and artist names are made up, and their music numbers are examples, not measurements from real recordings. The file doesn't tell us what people like, skip, save, or put in playlists. It also doesn't include lyrics or everything that can make a song special.

---

## 5. Strengths

<!--
Where does your system seem to work well

Prompts:

- User types for which it gives reasonable results
- Any patterns you think your scoring captures correctly
- Cases where the recommendations matched your intuition
-->

SongsMatcher 1.0 is easy to follow: songs that match the listener's genre and mood get points, and songs with a similar energy level get more energy points. The explanations show where the points came from. It works best when the listener's choices match the labels in the song list.

---

## 6. Limitations and Bias

<!--
Where the system struggles or behaves unfairly.

Prompts:

- Features it does not consider
- Genres or moods that are underrepresented
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users
-->

The catalog is small, with 20 songs across 17 genres, so many genres have only one example. The system also requires exact genre and mood matches, treating related labels like “pop” and “indie pop” as different. This can limit variety and miss songs a listener might enjoy, especially when their preferences are not well represented in the catalog.

---

## 7. Evaluation

<!--
How you checked whether the recommender behaved as expected.

Prompts:

- Which user profiles you tested
- What you looked for in the recommendations
- What surprised you
- Any simple tests or comparisons you ran

No need for numeric metrics unless you created some.
-->

I tested four profiles: pop/happy with energy `0.80`, rock/sad with energy `0.95`, pop/chill with energy `0.42`, and pop/happy with energy `0.95` plus a preference for acoustic music. I compared the top five from each profile using the current weights, which give energy more points than genre. I was surprised that the pop/chill profile had no songs in common with any of the other profiles' top fives, and that its first choice was lofi rather than pop.

- **Original vs. rock/sad:** Both lists include “Gym Hero” and “Golden Hour Groove,” but the rock/sad list adds “Storm Runner” and “Iron Horizon,” whose energy is close to `0.95`; none of the songs has a sad mood label.
- **Original vs. pop/chill:** The lists have no songs in common. The chill profile favors chill songs such as “Midnight Coding” and “Library Rain,” whose mood and energy fit, even though their genre is not pop.
- **Original vs. pop/happy/acoustic:** Both lists include “Sunrise City,” “Rooftop Lights,” and “Gym Hero.” The higher energy target and acoustic bonus change the remaining picks, although energy points still outweigh the acoustic bonus.
- **Rock/sad vs. pop/chill:** The lists have no songs in common: the first profile seeks high energy and rock, while the second favors chill mood and low energy.
- **Rock/sad vs. pop/happy/acoustic:** They share “Gym Hero,” “Iron Horizon,” and “Storm Runner,” all high-energy songs. The pop/happy profile instead brings in “Sunrise City” and “Rooftop Lights” for their pop and happy matches.
- **Pop/chill vs. pop/happy/acoustic:** The lists have no songs in common because the profiles favor different moods and energy levels; the acoustic preference applies only to the pop/happy profile.

These comparisons show the rankings respond to the selected mood and energy, but they do not prove which list is more accurate because I did not compare the results with actual listener feedback.

---

## 8. Future Work

<!--
Ideas for how you would improve the model next.

Prompts:

- Additional features or preferences
- Better ways to explain recommendations
- Improving diversity among the top results
- Handling more complex user tastes
-->

Next, I would add more tests to make sure the scores and song order are right. I would add more songs, and teach SongsMatcher 1.0 that some genres are related. I could also let listeners choose more song details, like tempo, and make sure the top picks aren't all too similar.

---

## 9. Personal Reflection

<!--
A few sentences about your experience.

Prompts:

- What you learned about recommender systems
- Something unexpected or interesting you discovered
- How this changed the way you think about music recommendation apps
-->

My biggest learning moment was seeing how changing the scoring weights shifts the scores and can change which songs rank highest, even though the formula is simple. I used an AI coding assistant to help adjust the profiles and weights and describe the results, but I needed to run the program and check the score explanations rather than assume its claims about the rankings were correct. I was surprised that exact matches for genre, mood, and energy can make a short list of songs feel like personalized recommendations, even though the system does not know what a listener actually enjoys. If I extended the project, I would add more songs, account for related genres, and test the recommendations with real listener feedback.
