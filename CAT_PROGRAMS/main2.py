import pandas as pd
from IPython.display import display
from sklearn.naive_bayes import MultinomialNB
import urllib.request
from textblob import TextBlob
import seaborn as sns
import numpy as np

biden_df = pd.read_csv("../myData/joebiden.csv", nrows=2300)
print(biden_df)

trump_df = pd.read_csv("../myData/hashtag_donaldtrump.csv", nrows=2300)
print(trump_df)
trump_df = trump_df[["tweet", "likes", "source", "user_name"]]
print(trump_df.head(20))
print(type(trump_df["tweet"]))
trump_df["tweet"] = trump_df["tweet"].apply(lambda x: str)

biden_df = biden_df[["tweet", "likes", "source", "user_name"]]
print(biden_df.head(20))
print(type(biden_df))

print(type(biden_df["tweet"]))
#testing using sentiment function from textblol library
biden_df["tweet"] = biden_df["tweet"].apply(lambda x: str(x))
print(type(biden_df["tweet"]))
print("Columns of the biden_df")
print(biden_df.columns)
print(biden_df.info())
print(biden_df.dropna().sum())
print(biden_df.info())
print(biden_df.head(20))

print(TextBlob(trump_df.at[9,"tweet"]).sentiment)

def polarity(review):
    return TextBlob(review).sentiment.polarity

trump_df["Polarity"] = trump_df["tweet"].apply(polarity)
biden_df["Polarity"] = biden_df["tweet"].apply(polarity)

# print(trump_df.head(20))
# print(biden_df.head(20))

trump_df["Expression"] = np.where(trump_df["Polarity"] > 0, "Positive", "Negaive")
trump_df.loc[trump_df.Polarity == 0, "Expression"] = "Neutral"
print(trump_df)

biden_df["Expression"] = np.where(biden_df.Polarity > 0, "Positive", "Negative")
biden_df.loc[biden_df.Polarity == 0, "Expression"] = "Neutral"
print(biden_df)

#need to know isna()
print(trump_df.isna().sum())
def graph(reviews):
    grouped_data = reviews.groupby("Expression").count()
    print(grouped_data)
graph(trump_df)
