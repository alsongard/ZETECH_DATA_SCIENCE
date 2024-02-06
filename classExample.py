import pandas as pd 
import matplotlib.pyplot as plt

data_df = pd.read_csv("./myData/classExample.csv")
print(data_df)
print(data_df.info())
print(f"dtype of var data_df is {data_df.dtypes}")
print(data_df.describe())
print("\n")

print(data_df.duplicated())
print("\n")

duplicates = data_df["Department"].duplicated()
print(data_df[duplicates])
print(data_df[duplicates].shape)

#using value_count() method 2 check number of times repeated
answers = data_df["Department"].value_counts()
print(answers)

#count users values
answers = data_df["Department"].duplicated(keep=False).value_counts()
print(answers)

#finding and replacing values
new_data_df = pd.read_csv("./myData/newClass.csv")
print(new_data_df.isnull())

returnValues = new_data_df.isnull()
print(returnValues.sum())

new_data_df = new_data_df.fillna("Human Resource Department")
print(new_data_df)

#visualizing the unique counts
#use department
# use data_df
unique_counts = data_df["Department"].value_counts()
print(unique_counts)
plt.figure(figsize=(5,4))
unique_counts.plot(kind="bar", color="skyblue")
plt.title(f"Unique counts of Department is:")
plt.xlabel("department")
plt.ylabel("Count")
plt.show()

print("\n")
unique_counts_gender = data_df.Gender.value_counts()
print(f"the gender summations is :")
print(unique_counts_gender)
plt.figure(figsize=(5,4))
unique_counts_gender.plot(kind="bar", color="blue")
plt.title(f"Unique counts on gender is :")
plt.xlabel("gender")
plt.ylabel("number count")
plt.show()

#pie chart on unique_counts
# plt.pie(unique_counts,labels="unique_counts.index", explode=(0.02,0.02,0.02,0.02,0.02), startangle=90, autopct="%1.1f%%", colors=["green","blue","skyblue","ligtcoral","red"])
# plt.title("Unique counts of departments")
# plt.axis("equal")
# plt.show()

print("\n")
print(data_df.head(8))