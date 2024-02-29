import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
from  IPython.display import display
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib
import pickle 


data_df = pd.read_csv("./myData/boston-housing-dataset.csv")
print(data_df.shape)#506 rows , 15columns

print(data_df.head(10))
with pd.option_context("display.max_rows",506):
    display(data_df)

#grab data from both columns
data_col_df = data_df.loc[:,["LSTAT","MEDV"] ]
print(data_col_df.head())

#visualization
color = ["orange", "red"]
data_df.plot(x="LSTAT", y="MEDV", style="o", color=color)
plt.xlabel("LSTAT")
plt.ylabel("MEDV")
plt.show()
# plt.legend[("lstat","medv")]


#adding linear regression line
regressor = LinearRegression()
x = pd.DataFrame(data_df["LSTAT"])
y = data_df["MEDV"]
regressor.fit(x, y)

data_df.plot(x="LSTAT",y="MEDV", style="o", label="Data Points")
#overlay the regression line
plt.plot(x, regressor.predict(x), color="red", lw=2, label="Regression Line")
plt.xlabel("LSTAT")
plt.ylabel("MEDV")
plt.show()

#divide data into independent and dependent variables
x_df = pd.DataFrame(data_df["LSTAT"])
y_df = pd.DataFrame(data_df["MEDV"])

#split data
X_train,X_test,Y_train,Y_test = train_test_split(x_df,y_df, test_size=0.2, random_state=1)
print(X_train)
print(X_test)
print(Y_train)
print(Y_test)

#training the algorithm
regressor.fit(X_train,Y_train)

#retrieving the intercept
print("Intercept Point")
print(regressor.intercept_)#when independent variable is 0

#retrieve the slope
print("retrieving the slope")
print(regressor.coef_)

#predicting values
y_pred = regressor.predict(X_test)
print(y_pred)


#evalueating the model
mae = metrics.mean_absolute_error(Y_test,y_pred)
mse = metrics.mean_squared_error(Y_test,y_pred)
rmse = np.sqrt(mse)#square root of mean squared errro

print(f"Mean Absolute Error : {mae}")
print(f"Mean Squared Error : {mse}")
print(f"Root Mean squared Error : {rmse}")

model = LinearRegression()
model.fit(X_train,Y_train)
joblib.dump(model, "Linear_regression_model.pkl")
# with open("Linear_regression_model.pkl", "wb") as file:
#     pickle.dump(model, file)


#testing the saved model
new_X = np.array([5,6,7,8,9,10]).reshape(-1, 1)#reshaped into a 2D array
print("new_X : 2D ARRAY")
print(new_X)
models = joblib.load("./Linear_regression_model.pkl")
predictions = models.predict(new_X)
new_data = pd.DataFrame({"X": new_X.flatten(), "Predicted_Y":predictions.flatten()})
print(new_data)