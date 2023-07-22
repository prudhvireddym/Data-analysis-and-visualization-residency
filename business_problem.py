import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")


# Load the cleaned data
data_cleaned = pd.read_csv('csvs/merged_cleaned_country.csv')


# Explode the 'genre' column into multiple rows
data_exploded = data_cleaned.assign(genre=data_cleaned['genre'].str.split(', ')).explode('genre')

# Create a boxplot of 'rating' for each 'genre' in top 10 Genre
plt.figure(figsize=(12, 6))
sns.boxplot(data=data_exploded, x='rating', y='genre', 
            order=data_exploded['genre'].value_counts().index[:10],
            palette="vlag")

plt.title(f'Rating vs Genre (Total: {len(data_exploded)} rows)', fontsize=20)
plt.xlabel('Rating', fontsize=15)
plt.ylabel('Genre', fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()
plt.savefig('business_visualization/rating_vs_genre.png')
plt.show()



#2 length vs rating# Separate movies and TV shows
movies = data_cleaned[data_cleaned['type'] == 'Movie'].copy()
tv_shows = data_cleaned[data_cleaned['type'] == 'TV Show'].copy()

# Convert duration to integer
movies['duration_int'] = movies['duration'].str.replace(' min', '').astype(int)
tv_shows_seasons = tv_shows[tv_shows['duration'].str.contains('Season')].copy()
tv_shows_seasons['duration_int'] = tv_shows_seasons['duration'].str.replace(' Season[s]?', '', regex=True).astype(int)

# Create a scatterplot for movies
plt.figure(figsize=(14, 8))
sns.scatterplot(data=movies, x='duration_int', y='rating', hue='rating', palette='coolwarm', alpha=0.6)
plt.title(f'Rating vs. Duration for Movies (Total: {len(movies)} rows)', fontsize=20)
plt.xlabel('Duration (minutes)', fontsize=15)
plt.ylabel('Rating', fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig('business_visualization/rating_vs_duration_movies.png')
plt.show()

# Create a scatterplot for TV shows
plt.figure(figsize=(14, 8))
sns.scatterplot(data=tv_shows_seasons, x='duration_int', y='rating', hue='rating', palette='coolwarm', alpha=0.6)
plt.title(f'Rating vs. Duration for TV Shows (Total: {len(tv_shows_seasons)} rows)', fontsize=20)
plt.xlabel('Duration (seasons)', fontsize=15)
plt.ylabel('Rating', fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig('business_visualization/rating_vs_duration_tv_shows.png')
plt.show()










