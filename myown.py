import pandas as pd
import matplotlib.pyplot as plt


movie = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')


print(movie.head())
print(ratings.head())
print(movie.isnull().sum())
print(ratings.isnull().sum())

ratings.drop_duplicates(inplace=True)

data = pd.merge(movie,ratings, on='movieId')
print( data.head())

data['genres'] = data['genres'].str.split('|')
# Flatten and one-hot encode
genres_exploded = data.explode('genres')
genres_encoded = pd.get_dummies(genres_exploded['genres'])
data = pd.concat([genres_exploded, genres_encoded], axis=1)
# Normalize ratings (e.g., mean-centered)
data['Normalized_Rating'] = data.groupby('userId')['rating'].transform(lambda x: x - x.mean())
# Create pivot table
interaction_matrix = data.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
# Remove movies with fewer than 10 ratings
movie_counts = data['movieId'].value_counts()
popular_movies = movie_counts[movie_counts >= 10].index
data = data[data['movieId'].isin(popular_movies)]

# Fill missing values with global average
interaction_matrix = interaction_matrix.apply(lambda x: x.fillna(x.mean()), axis=1)

data['Normalized_Rating'].plot(kind='bar',figsize=(14,6))
plt.show()