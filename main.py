# Import the required library
import pandas as pd
from rapidfuzz import fuzz, process


data_netflix = pd.read_csv('netflix_original_8810.csv')
data_imdb = pd.read_csv('netflix_imdb_9958.csv')

def common_titles():
    common_titles = set(data_netflix['title']).intersection(set(data_imdb['title']))

    num_common_titles = len(common_titles)

    print(f"There are {num_common_titles} titles that match in both the Netflix and IMDb datasets.")
#There are 3,169 titles that match in both the Netflix and IMDb datasets.




# Create a dictionary for faster lookup from Netflix data
netflix_dict = data_netflix.set_index('title').to_dict(orient='index')
print(netflix_dict['Dick Johnson Is Dead'])

# Function to find the best match in Netflix data
def find_best_match(title):
    best_match = process.extractOne(title, data_netflix['title'], scorer=fuzz.token_sort_ratio)
    if best_match[1] >= 95:
        return best_match[0]
    else:
        return None

# Apply the function to the IMDb data
data_imdb['best_match'] = data_imdb['title'].apply(find_best_match)
data_imdb.to_csv('data_imdb_Best_match_column.csv', index=False)


#Add the columns from Netflix data to IMDb data
for idx,col in enumerate(['country', 'show_id','type']):
    data_imdb[col] = data_imdb['best_match'].map(netflix_dict).apply(lambda x: x[col] if isinstance(x, dict) else None)

data_imdb.to_csv('data_imdb__initial_combined.csv', index=False)

# Replace NaN values in 'certificate' and 'duration' columns
data_imdb['certificate'] = data_imdb['certificate'].fillna(data_imdb['best_match'].map(netflix_dict).apply(lambda x: x['rating'] if isinstance(x, dict) else None))
data_imdb['duration'] = data_imdb['duration'].fillna(data_imdb['best_match'].map(netflix_dict).apply(lambda x: x['duration'] if isinstance(x, dict) else None))

# Remove the 'best_match' column
data_imdb = data_imdb.drop(columns=['best_match'])

# Save the result as a CSV file
data_imdb.to_csv('merged_data.csv', index=False)



def clean_merged(merged_csv):
    # Load the merged data
    data_merged = pd.read_csv('merged_data.csv')

    # Remove rows where the 'country' column is missing
    data_cleaned = data_merged.dropna(subset=['country'])

    # Save the cleaned data to a new CSV file
    data_cleaned.to_csv('merged_cleaned_country.csv', index=False)



clean_merged('merged_data.csv')