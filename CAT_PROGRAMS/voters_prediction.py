import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from IPython.display import display
from sklearn.naive_bayes import MultinomialNB
data_df = pd.read_csv("../myData/tweets.csv")
print(data_df.head(15))

#check columns and data_set properties
print(data_df.columns)
print(data_df.shape)
print("checking for null values")
print(data_df.info())

#the data_set contains different languages filter data only containing english
data_bools = data_df["lang"]  == "en"
data_df = data_df[data_bools]#return new_values

#extract only the required features for the data set
data_df = data_df[["id", "handle", "text"]]

#drop null values 
#the dropna will drop any row containing null values
data_df = data_df.dropna()
#checking for null values

print(data_df.isnull())
#filter only the required columnss


# print(data_df.shape)
# print(data_df.info())

