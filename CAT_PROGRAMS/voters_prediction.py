import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import CountVectorizer
from sklearn.metrics import classification_report
from IPython.display import display
from sklearn.naive_bayes import MultinomialNB


pd.read