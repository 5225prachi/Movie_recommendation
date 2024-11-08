import pandas as pd

# Load the ratings data
ratings = pd.read_csv(r'ml-100k\ml-100k\u.data', delimiter='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])

movies = pd.read_csv(r'ml-100k\ml-100k\u.item', delimiter='|', encoding='ISO-8859-1', header=None, usecols=[0, 1])
movies.columns = ['movie_id', 'movie_title']

# Calculate the average rating for each movie
movie_ratings = ratings.groupby('item_id').agg({'rating': ['mean', 'count']})
movie_ratings.columns = ['average_rating', 'rating_count']

# Merge with the movie titles
movie_ratings = movie_ratings.merge(movies, left_index=True, right_on='movie_id')

# Display the first few rows to verify
print(movie_ratings.head())
