import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data_credits = pd.read_csv('tmdb_5000_credits.csv')
data_movies = pd.read_csv('tmdb_5000_movies.csv')

data_credits.head(3)
data_movies.head(3)

print(data_credits.shape)
print(data_movies.shape)

print(data_credits.columns)
print(data_movies.columns)

data_movies.rename(columns={'id':'movie_id'}, inplace=True)
print(data_movies.columns)

data_all = data_movies.merge( data_credits, on='movie_id')
print(data_all.shape)
data_all.head(3)
print(data_all.columns)

data_all.drop(columns=['homepage', 'budget', 'production_countries','release_date', 'status','production_countries'], inplace=True)
print(data_all.head(3))

print(data_all['overview'].head(3))
print(data_all['overview'].isnull().any())
print(data_all['overview'].isnull().sum())
data_all.dropna(inplace=True)
print(data_all['overview'].isnull().any())

#removing english words (the, a, an etc.)
cleanEnglishOverviewData = TfidfVectorizer(stop_words='english')
cleanEnglishOverviewData.matrix = cleanEnglishOverviewData.fit_transform(data_all['overview'])
print(cleanEnglishOverviewData.matrix.shape)

#cosine similarity
cosine_similarity = linear_kernel(cleanEnglishOverviewData.matrix, cleanEnglishOverviewData.matrix)

#remove repetitive movies
indices = pd.Series(data_all.index, index=data_all['original_title']).drop_duplicates()

def get_recommendations(title, cosine_similarity=cosine_similarity):
    if title not in indices:
        return "Movie not found"
    idx = indices[title]
    #similarity scores
    sim_scores = list(enumerate(cosine_similarity[idx]))
    #sorting by similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    #top 10 movies
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return data_all['original_title'].iloc[movie_indices]
input_movie = input("Enter movie name: ")
print(get_recommendations(input_movie))