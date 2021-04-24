import csv
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("mobile.csv")

graph = ff.create_distplot([df["AvgRating"].tolist()], ["Ratings"])
graph.show()
