import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from IPython.display import display
from sklearn.naive_bayes import MultinomialNB
import urllib.request
from textblob import TextBlob
import seaborn as sns


# urllib.request.urlretrieve("/kaggle/input/us-election-2020-tweets/hashtag_donaldtrump.csv", "../myData/hashtagtrump.csv")#not working link error
data_df = pd.read_csv("../myData/tweets.csv")
print(data_df)

# check columns and data_set properties
print(data_df.columns)
print("\n")
print(data_df.shape)
print("\n")
print("checking for null values")
print(data_df.info())


#select rows of data that will be used for our data analysis
#filter rows only with language as engliesh
data_df = data_df[data_df["lang"] == "en"]
data_df = data_df[["handle", "text"]]
print(data_df.isnull().sum())
print(data_df)
#drop every row containing null values
# data_df = data_df.dropna()
# print("After droping rows with null values")
# print(data_df)
'''
#the data_set contains different languages filter data only containing english
data_bools = data_df["lang"]  == "en"
data_df = data_df[data_bools]#return new_values

#extract only the required features for the data set
# data_df = data_df[["id", "handle", "text"]]

#drop null values 
#the dropna will drop any row containing null values
data_df = data_df.dropna()

#checking for null values
print(data_df.isnull())

#write to another file
# data_df.head(3400).to_csv("../myData/twitterElectionData.csv",index=False)
'''
