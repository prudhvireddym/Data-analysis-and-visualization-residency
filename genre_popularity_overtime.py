import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import imageio
import numpy as np
from PIL import Image

# Load the cleaned data
data_cleaned = pd.read_csv('csvs/merged_cleaned_country.csv')

# Strip leading and trailing spaces
data_cleaned['date_added'] = data_cleaned['date_added'].str.strip()

# Convert 'date_added' to datetime and extract the year
data_cleaned['date_added'] = pd.to_datetime(data_cleaned['date_added'], format="%B %d, %Y")
data_cleaned['year_added'] = data_cleaned['date_added'].dt.year

# Explode the 'genre' column into multiple rows
data_exploded = data_cleaned.assign(genre=data_cleaned['genre'].str.split(', ')).explode('genre')

# Prepare the data for the GIF
gif_data_genre = data_exploded.groupby(['year_added', 'genre']).size().reset_index(name='content_count')

# Filter for the top 10 genres
top_genres = gif_data_genre['genre'].value_counts().index[:10]
gif_data_genre = gif_data_genre[gif_data_genre['genre'].isin(top_genres)]

# Create a list of frames (one frame per year)
frames_genre = []
for year in gif_data_genre['year_added'].unique():
    year_data_genre = gif_data_genre[gif_data_genre['year_added'] == year]
    plt.figure(figsize=(10, 8))  # Set the figure size
    frame_genre = sns.barplot(data=year_data_genre, y='genre', x='content_count', orient='h', ci=None)
    frame_genre.set_xlim(0, gif_data_genre['content_count'].max())
    frame_genre.set_title(f'Genre Popularity in {int(year)}')
    plt.tight_layout()
    frame_genre.figure.canvas.draw()
    image_genre = np.frombuffer(frame_genre.figure.canvas.tostring_rgb(), dtype='uint8').reshape(frame_genre.figure.canvas.get_width_height()[::-1] + (3,))
    frames_genre.append(image_genre)
    plt.close()

# Save the frames as a GIF
imageio.mimsave('gif_visualization/genre_popularity_over_time.gif', frames_genre, duration=500)
