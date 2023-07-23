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

# Filter the data for the top 10 countries in terms of content count
top_countries = data_cleaned['country'].value_counts().index[:10]
data_cleaned_top_countries = data_cleaned[data_cleaned['country'].isin(top_countries)]

# Prepare the data for the GIF
gif_data = data_cleaned_top_countries.groupby(['year_added', 'country']).size().reset_index(name='content_count')

# Create a list of frames (one frame per year)
frames = []
for year in gif_data['year_added'].unique():
    year_data = gif_data[gif_data['year_added'] == year]
    plt.figure(figsize=(20, 15))  # Set the figure size
    frame = sns.barplot(data=year_data, y='country', x='content_count', orient='h', errorbar=None)
    frame.set_xlim(0, gif_data['content_count'].max())
    frame.set_title(f'Country-wise Content in {int(year)}', fontsize=16)
    plt.xlabel('Content Count', fontsize=14)
    plt.ylabel('Country', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout(pad=3)  # Increase padding
    frame.figure.canvas.draw()
    image = np.array(Image.frombytes('RGB', frame.figure.canvas.get_width_height(), 
                                     frame.figure.canvas.tostring_rgb(), 'raw', 'RGB', 0, 1))
    frames.append(image)
    plt.close()

# Save the frames as a GIF
imageio.mimsave('gif_visualization/country_wise_content_over_time.gif', frames, duration=1000)
