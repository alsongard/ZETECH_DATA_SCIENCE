import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from IPython.display import display
from sklearn.naive_bayes import MultinomialNB
import urllib.request



#read again the data
election_df = pd.read_csv("../myData/newElectionDataSet.csv")
print(election_df.head(20)) 

filter data to get 2 columns
data_df = election_df[["handle","text"]]
print(data_df)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(election_df["text"])
print(X)

splitting the data
y = election_df["handle"]
X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2)
print("data from X_train")
print(X_train)
print("data from X_test")
print(X_test)
print("Data from Y_test")

training the model
clf = MultinomialNB()

clf.fit(X_train, y_train)

#model evaluation
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

