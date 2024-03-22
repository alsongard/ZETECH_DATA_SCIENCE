import pandas as pd
from IPython.display import display
data_df = pd.read_csv("../myData/joebiden.csv", nrows=1200)
data_df = data_df[["tweet_id", "tweet", "likes", "source"]]
data_df = data_df.dropna()
print(data_df.shape)

# data_df.to_csv("../myData/twitterUSOpinion.csv") already created

#append data
trump_data_df = pd.read_csv("../myData/hashtag_donaldtrump.csv", nrows=1200)
print(trump_data_df)
trump_data_df = trump_data_df[["tweet_id", "tweet", "likes", "source"]]
trump_data_df = trump_data_df.dropna()

print(trump_data_df.columns)

#append data
# trump_data_df.to_csv("../myData/twitterUSOpinion.csv", mode="a", header=False) already added


# with pd.option_context("display.max_rows", 1200):
#     display(data_df[["tweet", "likes", "source"]])

#select only 1000 rows from the data set
#create a new dataset file
# with open("../myData/joebiden.csv") as input_file:
#     data = [next(input_file) for _ in range(1200)]


