"""
    this file will be used for testing isnull() and fillna() and using .at[].
    isnull() : is used to return True for rows of a dataframe whose value are Nan/null
    to replace data in this sections one can use:
    .fillna(valueUzd2replace)
    .at[rowIndexNumber, "columnName"] = asignData
"""
import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv("./myData/studentManipulatedData.csv")
print(data_df)
print("\n")

#using isnull() method
data = data_df.isnull()
print("data_df dataframe boolean values:")
print(data)
print(data_df.isnull().sum())

#filling in data of nan(not a number)
filledNullValues = data_df.fillna(21)
print(filledNullValues)

#filling in with a specific value for a row: 
#using .at()
data_df.at[2, "Test Score"] = 79
data_df.at[6, "Age"] = 20
print(data_df)
print(data_df.shape)

print("\n")

##acquiring EDA exploratory data analysis
print("Provide statistical data :")
print(data_df.describe())

print("\n")

print("Use the value_counts() method to get:")
print(data_df.Age.value_counts())

print("Use the value_counts() method to get:")
print(data_df["Test Score"].value_counts())

print("Use the value_counts() method to get:")
print(data_df["PassedExam"].value_counts())

print("Use the info() to see datatypes and :")
print(data_df.info())