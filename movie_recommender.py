import pandas as pd

# Load the ratings data
ratings = pd.read_csv(r'ml-100k\ml-100k\u.data', delimiter='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])

# Load the movies data
movies = pd.read_csv(r'ml-100k\ml-100k\u.item', delimiter='|', encoding='ISO-8859-1', header=None, usecols=[0, 1])
movies.columns = ['movie_id', 'movie_title']


# Display the first few rows of each dataframe
print(ratings.head())
print(movies.head())
