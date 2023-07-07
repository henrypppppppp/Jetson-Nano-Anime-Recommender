import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
plt.show()
# Define chunk size for processing data in chunks
chunk_size = 5000

# Process rating data in chunks
rating_chunks = pd.read_csv('rating.csv', chunksize=chunk_size)
df = pd.concat(rating_chunks)

# Process anime data in chunks
anime_chunks = pd.read_csv('anime.csv', chunksize=chunk_size)
anime = pd.concat(anime_chunks)

# Merging user rating and anime data
df = pd.merge(df, anime.drop('rating', axis=1), on='anime_id')

# Create a sparse matrix from the dataframe
ratings_data = df[['user_id', 'anime_id', 'rating']]
ratings_matrix = csr_matrix((ratings_data['rating'], (ratings_data['user_id'], ratings_data['anime_id'])))

# Calculate similarity matrix
similarity_matrix = ratings_matrix.T * ratings_matrix

# Get recommendations for a specific anime
anime_id = anime[anime['name'] == 'Shingeki no Kyojin']['anime_id'].iloc[0]
similarity_scores = similarity_matrix[anime_id, :].toarray().flatten()

# Sort the similarity scores and get the top 10 similar anime indices
similar_anime_indices = np.argsort(similarity_scores)[::-1][:10]

# Get the similar anime names
similar_anime_names = anime.loc[similar_anime_indices, 'name']
print(similar_anime_names)
