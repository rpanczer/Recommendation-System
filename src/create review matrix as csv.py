import pandas as pd
import numpy as np

#Read dataset to table using pandas
data_table = pd.read_csv('movie_ratings.csv')

#create matrix of data table
ratings = pd.pivot_table(data_table, index='user_id', columns='movie_id', aggfunc=np.max)

#save to csv
ratings.to_csv("review_matrix.csv", na_rep="")
