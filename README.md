# 🎌 Anime Network Analysis

### A Three-Part Network Analysis of MyAnimeList

Welcome to our deep dive into the world of anime - not through streaming platforms, but through **networks, graphs, and communities**.

This project explores how anime, genres, and users connect inside MyAnimeList using network analysis. Instead of asking *“What is this anime about?”* we asked:

>* **How do genres cluster?**<br>
>* **How do anime bridge communities?**<br>
>*  **And how do users actually move through this ecosystem?**

---

## 🌟 The Big Idea

A previous study by [Sosa et al. (2024)](pdf/Analysis%20of%20Bipartite%20Networks%20in%20Anime%20Series-%20Textual%20Analysis,%20Topic%20Clustering,%20and%20Modeling.pdf) analysed anime communities using NLP on synopses. Cool idea... But after [exploring](pdf/NA_reading_presentation.pdf) their research we wondered:

🧐 Do summaries really drive user behavior?
Or do **genres, ratings, and completion habits** shape communities more strongly?

So we rebuilt the analysis using the same [Kaggle dataset](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020/discussion/352326), but with a different focus:

* 🎭 Genre co-occurrence
* 📺 Anime-genre bipartite mapping
* 👥 User preference structures

**Disclaimer**: 3/5 files from the dataset can be found in the data folder of this repo, the other two are very big so we suggest to open them using [RowZero](https://rowzero.com/), a spreadsheet tool for big data.

---

## 📦 Dataset

From the full dataset, we focused on:

* `anime_synopsis.csv` → for genre tags
* `rating_complete.csv` → only anime users marked as *completed*

Why only completed? Because someone who finishes an anime probably had a more stable viewing experience than someone who dropped it halfway.

To handle scale:

* The original dataset had 100+ million rows.
* We sampled **10,000 users** using `numpy.random.choice`.

---
# 🧠 Network 1: Genre Co-Occurrence

We built a weighted network where:

* **Nodes** = genres
* **Edges** = genres appearing together in the same anime
* **Weight** = how often they co-occur

📊 **Results:**<br><br>
<img src="about networks/network1_genre_communities.png" alt="Genre Co-Occurrence Network" width="600"/>
* 41 genres
* 726 connections
* Very dense network (low modularity ~0.12)

### 🔥 Main Findings

Both Greedy Modularity and Louvain detected **4 consistent communities**:

1. ⚔️ Action & Adventure
2. 💕 Romance & Slice of Life
3. 🌑 Dark & Psychological
4. 🎵 Niche

Low modularity isn’t a weakness! It shows that **anime genres heavily overlap**.

Examples:

* <i>Attack on Titan</i> → action + military + psychological
* <i>Your Lie in April</i> → romance + drama + slice of life
* <i>Sword Art Online</i> → action + game + romance

👉 Genres don’t exist in isolation, anime is inherently hybrid.

---

# 🎬 Network 2: Anime-Genre Mapping

We assigned each anime to the genre community most represented in its tags.

If an anime connected evenly across communities, it became a **bridge anime**.

### 💥 Key Insight

The strongest bridge wasn’t between Action & Dark.

It was between:

💕 Romance & Slice of Life
🎵 Niche

This suggests niche genres often blend into softer, character-driven storytelling.

✔️ Over 50% of anime had strong confidence (>0.75) in their assigned communities, supporting the structure.

---

# 👥 Network 3: User Preferences

Instead of simply assigning users to communities, we calculated:

> What percentage of a user’s completed anime belongs to each community?

This revealed two viewer types:

### 🌀 Generalists

Watch across multiple communities.

### 🎯 Specialists

Have >40% preference in one community.

### 📊 Main Results

* 💕 Romance & Slice of Life had the highest overall engagement.
* 🎵 Niche had the highest percentage of specialists.

👉 Fewer people watch niche anime, but those who do are highly committed!

---

# 🧩 What This Project Shows

Anime, genres, and users form a **tightly connected ecosystem**.

* Genres shape anime structure.
* Anime structure shapes user patterns.
* Users move across communities, but not equally.

Unlike synopsis-based NLP clustering, genre networks:

* Reflect platform structure
* Align with user behavior
* Avoid noisy keyword artifacts

---

# ⚠️ Limitations

* Data from 2020 (snapshot in time)
* Only MyAnimeList users (mostly Western / English-speaking)
* Based on Kaggle’s scraped dataset

Future expansions could include:

* Cross-platform comparison
* Longitudinal analysis
* NLP on user comments
* Image/video recognition of fan culture (AMVs, edits)

---

# 🛠️ Tools & Libraries

* Python
* Pandas
* NumPy
* NetworkX
* python-louvain
* Google Colab

---

# 🚀 Why This Matters

Recommendation systems often treat media as isolated items.

But anime isn’t isolated.

It’s:

* A cultural ecosystem
* A hybrid genre web
* A dynamic fan network

And sometimes, the strongest communities aren’t the biggest ones but the most devoted ones.

---

# 💬 Final Thought

If you’ve ever:

* Gone from a mecha anime to a romance unexpectedly
* Fallen into a niche genre spiral
* Or insisted you “only watch one type” but somehow don’t

You’re already part of the network.

---
# 🌟 Meet the Team

This project was developed by a group of five students in the [Network Analysis course (2025/26)](https://www.unibo.it/it/studiare/insegnamenti-competenze-trasversali-moocs/insegnamenti/insegnamento/2025/467048) taught by [Prof. Saverio Giallorenzo](https://saveriogiallorenzo.com/) at the University of Bologna for the MA degree in [DHDK](https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge):

* [Fahmida Islam](https://github.com/Fahmyrose)

* [Regina Manyara](https://github.com/ValkyrieCain9) 

* [Martina Marchesi](https://github.com/martinamrc) 

* [Rumana Mehboob](https://github.com/rumana-mh) 

* [Cristina Vercelli](https://github.com/cristinavercelli) 

---

✨ Built with curiosity, critique, and a lot of graph theory. Check out the full report [here](pdf/NA_report.pdf)!
