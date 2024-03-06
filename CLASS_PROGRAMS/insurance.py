import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler

data_df = pd.read_csv("../myData/insurance.csv")
print(data_df)
# with pd.option_context("display.max_rows",1338):
#     display(data_df)
#column data to use against insurance charges
age_df = data_df["age"]
print(age_df)
label_encoder = LabelEncoder()
data_df["smoker"] = label_encoder.fit_transform(data_df["smoker"])
data_df["sex"] = label_encoder.fit_transform(data_df["sex"])
print(data_df.head(20))

#generate a Feature matrix
# print(data_df[["age", "charges"]])
X = data_df[["age", "charges"]]
print(X)

#standardize the data
scalar = StandardScaler()
X_std = scalar.fit_transform(X)
print(X_std)

#Applying KMeans cluster
nu_cluster = 3
kmeans  = KMeans(n_clusters=nu_cluster,random_state=0)
data_df["cluster"] = kmeans.fit_predict(X_std)
print("after Kmeans predict")
print(data_df.head(30))
# visualization
plt.figure(figsize=(8,7))
for i in range(nu_cluster):
    cluster_data = data_df[data_df["cluster"] == 1]
    plt.scatter(cluster_data["charges"], cluster_data["age"],c=plt.cm.viridis(i/(nu_cluster -1)) ,label=f"Cluster {i + 1}")

plt.xlabel("Charges")
plt.ylabel("Age")
plt.title("Cluster of age against charges", fontsize=16, fontweight="bold")
plt.legend(loc="lower right")
plt.show()