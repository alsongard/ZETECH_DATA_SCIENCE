import matplotlib.pyplot as plt
import pandas as pd


data_df = pd.read_csv("./myData/users.csv")
print(data_df)

#plot variation of users salary
# plt.bar(x="Name", y="Salary" , data=data_df)
# plt.show()
apples = [10,3,7,6,7,4]
oranges = [1,14,2,5,8,3]

years=list(range(2000,2006))
print(years)
plt.plot(years,apples)
plt.plot(years,oranges)
plt.title("Fruits Production")
plt.legend(["apples","oranges"])
plt.show()