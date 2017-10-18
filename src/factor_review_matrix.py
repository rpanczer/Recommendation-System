import Pandas as pd
import Numpy as np

#Load user ratings into a data frame
user_ratings_df = pd.read_csv("movie_ratings.csv")

#Convert the running list of user ratings into a matrix
user_ratings_matrix = pd.pivot_table(user_ratings_df, index='user_id', columns='movie_id', aggfunc=np.max)

#Apply matrix factorization to find the latent features
U, M = matrix_factorization_utilities.low_rank_matrix_factorization(user_ratings_df.as_matrix(), num_features=15,
                                                                    regularization_amount=0.1)

# Find all predicting ratings by multiplyin the U by the M
predicted_ratings = np.matmul(U, M)

# Save all predicted ratings to a csv file
predicted_ratings_df = pd.DataFrame(index=user_ratings_matrix,
                                    columns=user_ratings_matrix.columns,
                                    data=predicted_ratings)
predicted_ratings_df.to_csv("predicted_ratins.csv")
