import pandas as pd
import numpy as np
import os
import webbrowser

# Read the dataset into a datatable using Pandas
data_table = pd.read_csv("movie_ratings.csv")

# Convert the running list of user ratings into a matrix using the 'pivot table' function
# Make sure you handle duplicates!! aggfunc
ratings_matrix = pd.pivot_table(data_table, index='user_id', columns='movie_id', aggfunc=np.max)

#Create a web page to view the data
#Make sure you handle NaN
html = ratings_matrix.to_html(na_rep="")

#save html to temp folder
with open("data_matrix.html", "w") as f:
    f.write(html)

#open in web browser
full_filename = os.path.abspath("data_matrix.html")
webbrowser.open("file://{}".format(full_filename))