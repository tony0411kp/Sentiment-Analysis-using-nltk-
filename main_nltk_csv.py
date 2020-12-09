# cleaning text steps
# 1) Create a text file and take text from it
# 2) convert the letter into lowercase ('Apple' is not equal to 'apple')
# 3) remove punctuations like . , ! ? etc.

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
text_file = str(list(df['content']))
text1 = open("sample.txt", "w")
n = text1.write(text_file)

text = open("sample.txt").read()
#text = open("read.txt",encoding='utf-8').read()
lower_case_text = text.lower()

cleaned_text = lower_case_text.translate(str.maketrans('','',string.punctuation))
# str1 : specifies the list of characters that need to be replaced 
# str2 : specifies the list of characters with which the charactersneed to be replaced
# str3 : specifies the list of characters that needs to be deleted 

tokenized_word = word_tokenize(cleaned_text,"english")

final_words = []
for word in tokenized_word:
    if word not in stopwords.words('english'):
        final_words.append(word)

# NLP emotion algorithm
# 1) check if the word in the final_words list is also present in the emotions.txt
#   -> firstly open the emotions file
#   -> loop through each line of emotions file and clear it
#   -> extract the word and emotion using split
# 2) if word is present -> add the emotion to emotions_list
# 3) count each emotion in emotions_list

emotions_list = []
with open('emotions.txt','r') as emotions_file:
    for line in emotions_file:
        cleared_line = line.replace('\n',"").replace(',',"").replace("'","").strip()
        word,emotion = cleared_line.split(':')

        print(f'word : {word} emotion : {emotion}')

        if word in final_words:
            emotions_list.append(emotion)
c = Counter(emotions_list)

def sentiment_analysed(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print ("NEGATIVE SENTIMENT")
    elif(pos > neg):
        print ("POSITIVE SENTIMENT")
    else:
        print ("NEUTRAL VIBE")

    fig1, ax1 = plt.subplots()
    ax1.pie(score.values(), labels=score.keys(), autopct='%1.1f%%')
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig1.autofmt_xdate()
    plt.savefig('piegraph_nltk_csv.png')
    plt.show()

'''# bar graph
fig , axis = plt.subplots()
axis.bar(c.keys(),c.values())
fig.autofmt_xdate()
plt.savefig('bargraph_nltk_csv.png')
plt.show()'''

sentiment_analysed(cleaned_text)

# pie chart
fig, axis = plt.subplots()
axis.pie(c.values(), labels=c.keys(), autopct='%1.1f%%')
# axis.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig('piegraph_nltk_csv.png')
plt.show()