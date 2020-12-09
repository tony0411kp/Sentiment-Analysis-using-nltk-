# cleaning text steps
# 1) Create a text file and take text from it
# 2) convert the letter into lowercase ('Apple' is not equal to 'apple')
# 3) remove punctuations like . , ! ? etc.

import os
import string 
from collections import Counter
import matplotlib.pyplot as plt

os.system('cls')

text = open("read.txt",encoding='utf-8').read()
lower_case_text = text.lower()

cleaned_text = lower_case_text.translate(str.maketrans('','',string.punctuation))
# str1 : specifies the list of characters that need to be replaced 
# str2 : specifies the list of characters with which the charactersneed to be replaced
# str3 : specifies the list of characters that needs to be deleted 

tokenized_word = cleaned_text.split() #splits into list of words

stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 
'but', 'by', 'can', 'did', 'do', 'does', 'doing', 'don', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 
'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just', 'me', 'more', 'most', 'my', 'myself', 'no', 'nor', 'not', 'now', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 's', 'same', 'she', 'should', 'so', 'some', 'such', 't', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'you', 'your', 'yours', 'yourself', 'yourselves']
['i', 'love', 'python']

final_words = []
for word in tokenized_word:
    if word not in stop_words:
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

        # print(f'word : {word} emotion : {emotion}')

        if word in final_words:
            emotions_list.append(emotion)
c = Counter(emotions_list)

# bar graph
fig , axis = plt.subplots()
axis.bar(c.keys(),c.values())
fig.autofmt_xdate()
plt.ylabel("no. of times")
plt.savefig('bargraph.png')
plt.show()
#pie chart
import numpy as np 
# Wedge properties 
wp = { 'linewidth' : 1, 'edgecolor' : "green" }  

fig, ax = plt.subplots() 
wedges, texts, autotexts = ax.pie(c.values(),  
                                  autopct = '%1.1f%%',   
                                  labels = c.keys(), 
                                  shadow = True,  
                                  startangle = 90, 
                                  wedgeprops = wp, 
                                  textprops = dict(color ="magenta"))
# Adding legend 
ax.legend(wedges, c.keys(), 
          title ="emotions", 
          loc ="center left", 
          bbox_to_anchor =(1, 0, 0.5, 1)) 
  
plt.setp(autotexts, size = 8, weight ="bold") 
ax.set_title("Customizing pie chart") 
  
# show plot 
plt.show()
'''
fig1, ax1 = plt.subplots()
ax1.pie(c.values(), labels=c.keys(), autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fig.autofmt_xdate()
plt.savefig('piegraph.png')
plt.show()
'''