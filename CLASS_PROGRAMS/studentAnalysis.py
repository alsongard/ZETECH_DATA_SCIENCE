import pandas as pd
import matplotlib.pyplot as plt

#read data 
data_df = pd.read_csv("./myData/studentMarks.csv")
print(data_df)

#checking with the duplicated() 
duplicate_data = data_df.duplicated()
print(data_df[duplicate_data])
# print(duplicate_data)

#passing specific columns to duplicated() mthd
data = data_df["Maths"].duplicated()
print(data_df[data])
