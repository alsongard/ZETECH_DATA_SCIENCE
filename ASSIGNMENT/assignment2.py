import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
from  IPython.display import display
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib
import pickle 
from IPython.display import display
# TRAFFIC ROAD ANALYSIS
data_df = pd.read_csv("../myData/trafficAccidents.csv")
print(data_df)
print("\n")

print("Severity: used to measure the damaging impact of the accident")
print("Maximum Severity is : {}".format(data_df.Severity.max()))
#use value counts to count the number of severity cases
print(data_df["Severity"].value_counts())
print("\n")

print("SORTING : column.sorting_values | dataframe.sort_values(column, ascending = true|flase)")
print(data_df.Severity.sort_values())#only sorted one column
print(data_df.sort_values("Severity", ascending=False).head(20))
print("\n")

#try to group data based on month
print(f'Type of our date time of accident is {type(data_df["Date Time of Accident"])} and the dytpe is {data_df["Date Time of Accident"].dtype}')
data_df["Date Time of Accident"] = pd.to_datetime(data_df["Date Time of Accident"])
#after conversion
print(f'Type of our date time of accident is {type(data_df["Date Time of Accident"])} and the dytpe is {data_df["Date Time of Accident"].dtype}')
print(data_df)
#add new columns of year, month, day
data_df["Year"] = pd.DatetimeIndex(data_df["Date Time of Accident"]).year
data_df["Month"] = pd.DatetimeIndex(data_df["Date Time of Accident"]).month
data_df["Day"] = pd.DatetimeIndex(data_df["Date Time of Accident"]).day#day of the month
data_df["Weekday"] = pd.DatetimeIndex(data_df["Date Time of Accident"]).weekday
print(data_df)

#performing value_counts() in Drug Test
print(data_df["Drug Test"].value_counts())
data_drug_df = data_df["Drug Test"] == 6
print(data_df[data_drug_df])

print("\n")
print("\n")
print("\n")

print(data_df)
##PLOTING THE DATA
data_df.plot(x="Drug Test", y="Severity", style="o", color="red", label="DATA")
plt.show()

#adding regression LIne
regressor = LinearRegression()
x = pd.DataFrame(data_df["Drug Test"])
y = data_df["Severity"]
regressor.fit(x,y)
data_df.plot(x="Drug Test", y="Severity", style="o" ,label="Regression Line7")
#overlaying the regression line
plt.plot(x, regressor.predict(x), color="red", lw=2, label="Regression Line")
plt.xlabel("Drug Test")
plt.ylabel("Severity")
plt.show()

#divide data into independent and dependent variables
x_df = pd.DataFrame(data_df["Drug Test"])
y_df = pd.DataFrame(data_df["Severity"])

#split data
X_train, X_test, Y_train, Y_test = train_test_split(x_df, y_df, test_size=0.2, random_state=1)

#train algorithm
regressor.fit(X_train,Y_train)

#predict values
y_pred = regressor.predict(X_test)
print(y_pred)

model = LinearRegression()
model.fit(X_train, Y_train)
joblib.dump(model, "./Linear_regression_model.pkl")
