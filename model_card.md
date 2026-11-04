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

The song list is small, so a listener might not find many songs they like. The system needs an exact genre or mood match: “pop” and “indie pop,” for example, count as different. Genre is worth the most points, so a genre match can matter more than a closer mood or energy match. Acousticness only matters if the listener chooses an acoustic preference.

SongsMatcher 1.0 doesn't know what people have actually listened to or enjoyed. It doesn't understand lyrics or why a song might feel meaningful. Its score is just a way to compare the song details in this project; it can't promise someone will like a song.

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

I tried the command-line example with pop, happy, and an energy target of `0.80`. `Sunrise City` came first with `99.40/100`, which made sense because its genre and mood match and its energy is close. I checked that the songs are sorted by score and that the screen shows the score and reasons.

I also checked the score math with and without an acoustic preference. The existing automatic tests pass, but they mostly check the separate `Recommender` class, not the scoring and ranking functions used by the command-line demo. Those parts could use more automatic tests.

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

I learned that a music picker can give songs points and put the highest-scoring ones first. Changing which things are worth more points can change the list. I also learned that a high score doesn't mean someone will definitely love a song—it only means the song matches the choices this little project checks. Music apps have to make choices about what to pay attention to, too.
