"""
    this file will be used for analysising the data from the interviewData.csv file in which we will plot graphs
"""
import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv("./myData/interviewData.csv")
print(data_df)

#check data type
print(f"the data type of the variable data_df is {type(data_df)}")

#take users who qualified(Q) plot a piechart against users who didnot qualify(NQ)

qualified_users = data_df["class"] =="Q" #returns boolean values
print(qualified_users)

#return only users who classified
print(data_df[qualified_users])
#return only users who did not qualify
unqualified_users = data_df["class"] == "NQ"
print(data_df[unqualified_users])
