# ELECTION PREDICTION SYSTEM
*******

# DESCRIPTION
These project is used to predict the chances of a candidate in winning an election. The Program uses textblob library to analyse the tweets from different users, and predict. The **main.py** file contains the whole program code. All other files were used for research and experimental and may be found in the research directory. 
Also using Naive bayes classifier failed. The project is on hold until **further notice**

*******
# Features

## Library used
1. TextBlob
>>> Textblob library is a library that is designed for  simpler natural language processing(NLP) tasks. The library will be used to analyse the tweets of the users. By using the sentiment property, which returns polarity and subjectivity of the statement, each with it's own value. For polarity providing values ranging from -1.0 to 1.0 with -1.0 being very negative, 0 being neutral and 1.0 being positive statement. Subjectivity on the other hand providing values ranging from 0.0 to 1. Text with values of beind 0.0 beind objective text or factual while text with values being closer to 1 indicates subjective text(opinion-based).

>>> After finding the sentiment characteristics of each text and adding it to the dataframe. We will use the Polarity value to determine which candidate is more likely to win the election