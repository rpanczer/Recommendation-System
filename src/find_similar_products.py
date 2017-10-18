import numpy as np
import pandas as pd
import matrix_factorization_utilities

#Load user ratings
user_ratings_df = pd.read_csv("movie_ratings.csv")

#Load movie titles
movie_titles_df = pd.read_csv("movie_index.csv")

#Create a matrix of user ratings
user_ratings_matrix = pd.pivot_table(user_ratings_df, index='user_id', columns='movie_id', aggfunc=np.max)

#Apply matrix factorization to find the latent features
U, M = matrix_factorization_utilities.low_rank_matrix_factorization(user_ratings_matrix.as_matrix(),
                                                                    num_features=15,
                                                                    regularization_amount=1.0)
#Transpose M
M = np.transpose(M)

#Choose a movie similar to movie # 5
movie_id =5

#Get movie 5s title and genra
movie_information = movie_titles_df.loc[5]

#Print title and genra
print("Title of movie " + movie_id + " is: {}".format(movie_information.title))
movie_title = movie_information.title
print("The genre of " + movie_title + "is: {}".format(movie_information.genre))



