import os
import string 
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize # for tokenising word
from nltk.corpus import stopwords # for importing stop words
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

os.system('cls')

df=pd.read_csv(r'text_emotion.csv')
emotions_list = list(df['sentiment'])
c = Counter(emotions_list)

fig1, ax1 = plt.subplots()
ax1.pie(c.values(), labels=c.keys(), autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig('piegraph_csv.png')
plt.show()

fig , axis = plt.subplots()
axis.bar(c.keys(),c.values())
fig.autofmt_xdate()
plt.ylabel("no. of times")
plt.savefig('bargraph_csv.png')
plt.show()