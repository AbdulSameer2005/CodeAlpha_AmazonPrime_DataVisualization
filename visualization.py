import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("amazon_prime_titles.csv")

# Style
sns.set_style("whitegrid")

# 1. Movies vs TV Shows
plt.figure(figsize=(6,4))
df["type"].value_counts().plot(kind="bar")
plt.title("Movies vs TV Shows on Amazon Prime")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("movies_vs_tvshows.png")
plt.show()

# 2. Top 10 Countries
plt.figure(figsize=(10,5))
df["country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries by Amazon Prime Content")
plt.xlabel("Country")
plt.ylabel("Titles")
plt.tight_layout()
plt.savefig("top_10_countries.png")
plt.show()

# 3. Content Ratings
plt.figure(figsize=(8,5))
df["rating"].value_counts().head(10).plot(kind="bar")
plt.title("Amazon Prime Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("ratings_distribution.png")
plt.show()

# 4. Release Year Trend
plt.figure(figsize=(10,5))
df["release_year"].value_counts().sort_index().tail(30).plot(kind="line")
plt.title("Content Release Trend")
plt.xlabel("Year")
plt.ylabel("Titles")
plt.tight_layout()
plt.savefig("release_year_trend.png")
plt.show()

# 5. Top Genres
genres = df["listed_in"].str.split(", ").explode()

plt.figure(figsize=(10,5))
genres.value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Genres on Amazon Prime")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("top_genres.png")
plt.show()

print("Data Visualization Project Completed Successfully!")