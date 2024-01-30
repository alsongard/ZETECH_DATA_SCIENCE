# this document will read data from a comma seperated value file
# we will be using pandas library module.

import pandas as pd
import matplotlib.pyplot as plt
data_df = pd.read_csv("./myData/medal.csv")
print(data_df)

#plot data 
plt.figure(figsize=(5,8))
plt.bar(data_df.country, data_df.medal)
plt.title("Country Medals")
plt.xlabel("Country Name")
plt.ylabel("Medal Number")
plt.show()

