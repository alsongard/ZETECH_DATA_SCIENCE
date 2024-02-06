import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv("./myData/studentPass.csv")
print(data_df)
print("\n")


#using edge to value_counts()
print("The number of ages repeated are shown:")
print(data_df.Age.value_counts())
print("\n")

print("Checking for duplicates in :")
print("\n")
print("Entire dataframe object:")
data = data_df.duplicated()
print(data_df[data])


print("Checking on Test Score column:")
data = data_df["Test Score"].duplicated()
print(data_df[data])
print(data_df["Test Score"].value_counts())

print("\n")
print("using counts to count duplicated data:")
AgeDuplicatedData = data_df["Age"].duplicated(keep=False).value_counts()
print(AgeDuplicatedData)

print("\n")

##ploting data using value_counts()
print("ploting data using value_counts()")
print(data_df)
unique_counts = data_df.PassedExam.value_counts()
plt.figure(figsize=(8,6))
unique_counts.plot(kind="bar", color="black")
plt.title("EDA for PassedExams")
plt.xlabel("ExamResult")
plt.ylabel("Counts")
plt.show()

print("\n")

print("Plotting data for pie chart using unique_counts on Age:")
unique_counts = data_df.Age.value_counts()
plt.figure(figsize=(8,8))
plt.pie(unique_counts,labels=unique_counts.index, autopct="%1.1f%%", colors=["black", "red", "green"], startangle=90, explode=(0.02,0.02,0.02))
plt.title("Student Age")
plt.show()