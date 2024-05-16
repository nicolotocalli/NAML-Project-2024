#Creation of Data points for clustering by favourite genres: 
exploded_movies = movies.assign(genres=movies['genres'].str.split('|')).explode('genres')
#Every user is a data point (a 4 dimensional vector), the features are userId, avg Drama rating, avg Comedy rating, avg Action rating
genre_ratings = ratings.groupby('userId').mean()

genre_ratings = genre_ratings.drop('movieId', axis=1)
genre_ratings = genre_ratings.drop('rating', axis=1)

genre_ratings = genre_ratings.reset_index()

genre_ratings['Romance'] = 0
genre_ratings['Sci-Fi'] = 0
genre_ratings['Adventure'] = 0

#change dtype of Drama, Comedy and Action to float
genre_ratings['Romance'] = genre_ratings['Romance'].astype(float)
genre_ratings['Sci-Fi'] = genre_ratings['Sci-Fi'].astype(float)
genre_ratings['Adventure'] = genre_ratings['Adventure'].astype(float)

for index, row in genre_ratings.iterrows():
    userId = row['userId']
    ratings_by_user = ratings[ratings['userId'] == userId]
    for genre in ['Romance', 'Sci-Fi', 'Adventure']:
        set_of_movies = exploded_movies[exploded_movies['genres'] == genre]
        Ids = set(set_of_movies['movieId'])
        ratings_by_genre = ratings_by_user[ratings_by_user['movieId'].isin(Ids)]
        avg_rating = ratings_by_genre['rating'].mean()
        genre_ratings.at[index, genre] = avg_rating

#drop NAN samples
genre_ratings = genre_ratings.dropna()

genre_ratings







#Creation of Data points for clustering by favourite tags: 
exploded_tags = tags.assign(tag=tags['tag'].str.split('|')).explode('tag')
#Every user is a data point (a 4 dimensional vector), the features are userId, avg comedy rating, avg ending rating, avg twist rating
tag_ratings = ratings.groupby('userId').mean()
tag_ratings = tag_ratings.drop('movieId', axis=1)
tag_ratings = tag_ratings.drop('rating', axis=1)

tag_ratings = tag_ratings.reset_index()

tag_ratings['funny'] = 0
tag_ratings['fantasy'] = 0
tag_ratings['mafia'] = 0

#change dtype of comedy, ending and twist to float
tag_ratings['funny'] = tag_ratings['funny'].astype(float)
tag_ratings['fantasy'] = tag_ratings['fantasy'].astype(float)
tag_ratings['mafia'] = tag_ratings['mafia'].astype(float)

for index, row in tag_ratings.iterrows():
    userId = row['userId']
    ratings_by_user = ratings[ratings['userId'] == userId]
    for tag in ['funny', 'fantasy', 'mafia']:
        set_of_tags = exploded_tags[exploded_tags['tag'] == tag]
        Ids = set(set_of_tags['movieId'])
        ratings_by_genre = ratings_by_user[ratings_by_user['movieId'].isin(Ids)]
        avg_rating = ratings_by_genre['rating'].mean()
        tag_ratings.at[index, tag] = avg_rating

#drop NAN samples
tag_ratings = tag_ratings.dropna()

tag_ratings