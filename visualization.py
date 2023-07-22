import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use seaborn styles
sns.set_theme(style="darkgrid")

# Load the cleaned data
data_cleaned = pd.read_csv('csvs/merged_cleaned_country.csv')

# 1. Rating Distribution
plt.figure(figsize=(12,6))
sns.histplot(data=data_cleaned, x="rating", kde=True, color='skyblue', bins=20)
plt.title(f'Histogram Plot Of Rating Distribution (Total: {len(data_cleaned)} Content)', fontsize=22)
plt.xlabel('Rating', fontsize=18)
plt.ylabel('Count', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('visualization/rating_distribution.png')
plt.show()

# 2. Top Genres
plt.figure(figsize=(12,6))
genres = data_cleaned['genre'].str.split(', ').explode()
sns.countplot(y=genres, order=genres.value_counts().index[:10], palette='viridis')
plt.title(f'Bar Plot of Top Genres (Total: {len(genres)} Genres)', fontsize=22)
plt.xlabel('Count', fontsize=18)
plt.ylabel('Genre', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(axis='x')
plt.tight_layout()
plt.savefig('visualization/top_genres.png')
plt.show()

# 3. Country-wise Content
plt.figure(figsize=(12,6))
sns.countplot(y=data_cleaned['country'], order=data_cleaned['country'].value_counts().index[:10], palette='viridis')
plt.title(f'Bar Plot of Country-wise Content (Total: {len(data_cleaned)} Content)', fontsize=22)
plt.xlabel('Count', fontsize=18)
plt.ylabel('Country', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(axis='x')
plt.tight_layout()
plt.savefig('visualization/country_wise_content.png')
plt.show()

# 4. Duration of Content
# Separate movies and TV shows
movies = data_cleaned[data_cleaned['type'] == 'Movie']
tv_shows = data_cleaned[data_cleaned['type'] == 'TV Show']

# Duration of Movies
plt.figure(figsize=(12,6))
movie_duration = movies['duration'].str.replace(' min', '').astype(int)
sns.histplot(movie_duration, kde=True, color='skyblue', bins=20)
plt.title(f'Histogram Plot of Duration of Movies (Total: {len(movies)} Movies)', fontsize=22)
plt.xlabel('Duration (minutes)', fontsize=18)
plt.ylabel('Count', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('visualization/duration_of_movies.png')
plt.show()

# Duration of TV Shows in Seasons
tv_shows_seasons = tv_shows[tv_shows['duration'].str.contains('Season')]
plt.figure(figsize=(12,6))
tv_show_season_duration = tv_shows_seasons['duration'].str.replace(' Season[s]?', '', regex=True).astype(int)
sns.histplot(tv_show_season_duration, kde=True, color='skyblue', bins=20)
plt.title(f'Histogram Plot of Duration of TV Shows (Seasons) (Total: {len(tv_shows)} rows)', fontsize=22)
plt.xlabel('Duration (seasons)', fontsize=18)
plt.ylabel('Count', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('visualization/duration_of_tv_shows_seasons.png')
plt.show()

# 5. Content Type
plt.figure(figsize=(12,6))
sns.countplot(x=data_cleaned['type'], palette='viridis')
plt.title(f'Bar Plot of Content Type (Total: {len(data_cleaned)} Content)', fontsize=22)
plt.xlabel('Type', fontsize=18)
plt.ylabel('Count', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('visualization/content_type.png')
plt.show()