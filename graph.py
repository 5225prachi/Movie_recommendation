import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the ratings data
ratings = pd.read_csv(r'ml-100k\ml-100k\u.data', delimiter='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])

# Load the movies data
movies = pd.read_csv(r'ml-100k\ml-100k\u.item', delimiter='|', encoding='ISO-8859-1', header=None, usecols=[0, 1])
movies.columns = ['movie_id', 'movie_title']

# Calculate the average rating for each movie
movie_ratings = ratings.groupby('item_id').agg({'rating': ['mean', 'count']})
movie_ratings.columns = ['average_rating', 'rating_count']

# Merge with the movie titles
movie_ratings = movie_ratings.merge(movies, left_index=True, right_on='movie_id')

# Filter movies with at least 50 ratings
popular_movies = movie_ratings[movie_ratings['rating_count'] > 50]

# Sort by average rating in descending order
popular_movies = popular_movies.sort_values(by='average_rating', ascending=False)

# Visualize the data with graphs
# Plot the distribution of movie ratings
plt.figure(figsize=(10, 6))
sns.histplot(ratings['rating'], bins=10, kde=True, color='blue')
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Plot the top 10 movies with highest average ratings
plt.figure(figsize=(10, 6))
sns.barplot(x='average_rating', y='movie_title', data=popular_movies.head(10), palette='viridis')
plt.title('Top 10 Movies by Average Rating')
plt.xlabel('Average Rating')
plt.ylabel('Movie Title')
plt.show()

# Plot the number of ratings for each movie
plt.figure(figsize=(10, 6))
sns.histplot(movie_ratings['rating_count'], bins=50, kde=False, color='green')
plt.title('Number of Ratings per Movie')
plt.xlabel('Number of Ratings')
plt.ylabel('Frequency')
plt.show()

# Plot the correlation between the number of ratings and average rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='rating_count', y='average_rating', data=movie_ratings, color='red')
plt.title('Correlation Between Rating Count and Average Rating')
plt.xlabel('Number of Ratings')
plt.ylabel('Average Rating')
plt.show()
