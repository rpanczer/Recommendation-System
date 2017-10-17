import pandas as pd
import os
import webbrowser

#Read dataset into data table with pandas
data_table = pd.read_csv("movie_index.csv", index_col="movie_id")

#Create a web page to view the data
html = data_table[0:25].to_html()

#save html to temp folder
with open("data2.html", "w") as f:
    f.write(html)

#open in web browser
full_filename = os.path.abspath("data.html2")
webbrowser.open("file://{}".format(full_filename))