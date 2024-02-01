"""
    this file will be used for analysising the data from the interviewData.csv file in which we will plot graphs
"""
import pandas as pd
import matplotlib.pyplot as plt

#read file using pandas
data_df = pd.read_csv("./myData/interviewData.csv")
print("the dataframe object data_df:")
print(data_df)
print("the info on the data frame object is:")
print(data_df.info())
print(f"the data type of the variable data_df is {type(data_df)}")#check data type
print("\n")

#take users who qualified(Q) plot a piechart against users who didnot qualify(NQ)
qualified_bool_users = data_df["class"] =="Q" #returns boolean values
print("the boolean values of qualified users")
print(qualified_bool_users)
qualified_users_df = data_df[qualified_bool_users]
print(qualified_users_df)#return only users who classified
print("\n")

#return only users who did not qualify
unqualified_bool_users = data_df["class"] == "NQ"
print("the boolean values of unqualified are : ")
print(unqualified_bool_users)
unqualified_users_df = data_df[unqualified_bool_users]
print(unqualified_users_df)
print("\n")

all_data_df = [data_df[unqualified_users]_df, data_df[qualified_users_df]]
print(all_data_df)
# plt.pie(all_data_df, labels=["qualified", "unqualified"], colors=["red", "green"])

plt.show()
