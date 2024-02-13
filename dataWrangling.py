"""
    this file will be used to show data wrangling,filtering techniques used in python

"""
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name" : ["Peter", "joyce", "George", "Phylis", "Moses", "Priscillah", "Eliud"],
    "Age" : [25,30,22,28,24,34,19],
    "Gender" : ["Male", "Female", "Male", "Female", "Male", "Female", "Male"],
    "Marks": [85,92,"Nan",88,"Nan",79,80]
}
myData = pd.DataFrame(data)
print(myData)#tabular data

#replace Nan values in the mark column
c = 0
sum = 0

for item in myData.Marks:
    print(type(item))
    if str(item).isnumeric():#check for any other mthds for comparison when it comes to data
        c+=1
        sum+=item

average = sum/c
print(average)
print("\n")

#use replace() attribute for a DataFrame object
myData1 = myData.replace(to_replace="Nan", value=average)
print("NEW DATA\n")
print(myData1)
print("\n")

#using map to replace values of the gender column to numbers 
newData = myData1
print("New dataframe object called newData :")
print(newData)
newData["Gender"] = newData.Gender.map({"Male":0, "Female":1}).astype(float)
print(newData)

#own
#myData["Gender"] = myData.Gender.replace({"Female":1.0, "Male":0.0})


#filtering data
#filter marks above 80
myData2 = myData1[myData1.Marks > 84]
print(myData2)
#drop a specific column use drop() mthd
myData2 = myData2.drop(["Age"], axis=1)
print(myData2)

#filtering data for top student using sort_values() method
myData3 = newData
print("New Dataframe object myData3")
print(myData3)
myData3.sort_values(by="Marks", ascending=False, inplace=True)
print(myData3)
print(myData3.head(3))

#wrangling and grouping methods