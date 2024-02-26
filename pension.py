import pandas as pd
import numpy as np
from IPython.display import display
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split



data_df = pd.read_csv("./myData/pension.csv")
print(data_df)
print(data_df.columns)
# with pd.option_context("display.max_rows", 100):
#     pd.display(data_df)

print("\n")
print("the selected columns are age and Pension")
data_col = data_df.loc[:,["Age","Pension"]]
print(data_col)

x = pd.DataFrame(data_df["Age"])
y = pd.DataFrame(data_df["Pension"])
print("See type of variable x and y")
print(type(x))
print(type(y))
print(f"the shape of x is {x.shape} and y is {y.shape}")
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=1)
#check shapes of x and y
print("check shapes of x and y")
print(f"X_train shape is {X_train.shape}")
print(f"X_test is {X_test.shape}")
print(f"y_train shape is {y_train.shape}")
print(f"y_test shape is {y_test.shape}")

# #load model
regressor = LinearRegression()
regressor.fit(X_train,y_train)
print(f"the value of regressor.intercept_ is {regressor.intercept_}")
print(f"the value of regressor.coef_ is {regressor.coef_}")

y_pred = regressor.predict(X_test)
print(f"the y_pred")
print(y_pred)