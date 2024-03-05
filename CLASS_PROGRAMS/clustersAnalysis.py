import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
import numpy as np
 

#Upload your dataset 

data_df = pd.read_csv("../myData/StudentsPerformance.csv")
print("dataframe objects")
print(data_df)
print("data_df columns:")
print(data_df.columns)


#check for any columns for null values
print(data_df.isnull().sum())
data_df["mean"] = data_df.loc[:, ["math score", "reading score", "writing score"]].mean(axis=1)
data_df["mean"] = round(data_df["mean"], 2)
#add grading to the column values
print(f"Maximum value of data_df.mean is {data_df['mean'].max()}")
print(f"Minimum value of data_df.mean is {data_df['mean'].min()}")

print("value counts of {}".format(data_df["mean"].value_counts()))

conditions = [
    (data_df["mean"] >= 97),
    (data_df["mean"] >= 93),
    (data_df["mean"] >= 90),
    (data_df["mean"] >= 87),
    (data_df["mean"] >= 83),
    (data_df["mean"] >= 80),
    (data_df["mean"] >= 77),
    (data_df["mean"] >= 73),
    (data_df["mean"] >= 70),
    (data_df["mean"] >= 63),
    (data_df["mean"] >= 60),
    (data_df["mean"] <= 59),

]
print(len(conditions))
grades = [4.0, 3.9, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.0, 0.7, 0.3]
print(len(grades))

data_df["grades"] = np.select(conditions, grades)
print(data_df)
print("value_counts of grades in the data set:")
print(data_df["grades"].value_counts)
