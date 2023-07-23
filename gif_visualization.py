# Import necessary libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# Load the updated data
data_cleaned_updated = pd.read_csv('csvs/merged_cleaned_country.csv')

# Strip leading and trailing spaces
data_cleaned_updated['date_added'] = data_cleaned_updated['date_added'].str.strip()

# Convert 'date_added' to datetime and extract year
data_cleaned_updated['date_added'] = pd.to_datetime(data_cleaned_updated['date_added'], format="%B %d, %Y")
data_cleaned_updated['year_added'] = data_cleaned_updated['date_added'].dt.year

# # Filter out rows with missing 'year_added'
# data_cleaned_updated = data_cleaned_updated.dropna(subset=['year_added'])

# # Convert 'year_added' to int for easy comparison
# data_cleaned_updated['year_added'] = data_cleaned_updated['year_added'].astype(int)

# # Sort values by 'year_added'
# data_cleaned_updated = data_cleaned_updated.sort_values('year_added')

# # Get the cumulative count of shows per year
# cumulative_count = data_cleaned_updated['year_added'].value_counts().sort_index().cumsum()

# # Prepare the figure
# fig, ax = plt.subplots()

# # Initialize the plot with the first year's data
# line, = ax.plot(cumulative_count.index[0], cumulative_count.iloc[0])

# ax.set_xlim(cumulative_count.index.min(), cumulative_count.index.max())
# ax.set_ylim(0, cumulative_count.max())

# ax.set_xlabel('Year')
# ax.set_ylabel('Cumulative Count')
# ax.set_title('Cumulative Count of Shows Added Over the Years')

# # Animation update function
# def update(num):
#     line.set_data(cumulative_count.index[:num+1], cumulative_count.iloc[:num+1])
#     return line,

# # Create the animation
# ani = animation.FuncAnimation(fig, update, frames=len(cumulative_count), interval=200)

# # Save the animation as a GIF
# ani.save('gif_visualization/cumulative_count.gif', writer='imagemagick')

# # Close the figure
# plt.close(fig)
