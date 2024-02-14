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
#create 2 dictionaries of student_details and fees_details
student_details = {
    "Name" : ["Peter", "Joyce", "George", "Phylis", "Moses", "Priscillah", "Eliud", "Veronicah", "John", "Juliet"],
    "Campus" :["Main","Ruiru","Nairobi","Main","Ruiru","Nairobi","Main","Ruiru","Nairobi","Main"],
    "IDNO" : [101,102,103,104,105,106,107,108,109,110]
}
fee_details = {
    "IDNO" : [101,102,103,104,105,106,107,108,109,110],
    "PENDING" : [6000,375,0,7640,3800,0,1250,900,5200,0]
    
}
fee_df = pd.DataFrame(fee_details)
student_df = pd.DataFrame(student_details)
print(fee_df)
#CONFIRMING THE LENGTH OF DICTIONARY ELEMENTS
print(len(student_details["Name"]))
print(len(student_details["Campus"]))
print(len(student_details["IDNO"]))
print(len(fee_details["PENDING"]))
#merging use pd.merge(dataFrameObject1,dataFrameObject2, on="COLUMN-NAME")

class_details = pd.merge(student_df,fee_df,on="IDNO")
print(class_details)