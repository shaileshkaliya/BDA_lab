# -*- coding: utf-8 -*-
"""word_count.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bMxDVjISA1EKwN5y8TUwaqvLUmBf52pE
"""

with open('file.txt',"r") as file:
    text = file.read()

print(text[:100])

import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords
nltk.download('stopwords')

# Get NLTK English stopwords
stop_words = set(stopwords.words('english'))

word_list = text.split()

special_symbols = '''!@#$%^&*()_+}{[];':"<>,.?/*-+.123456789'''

word_set = [word for word in word_list if word not in special_symbols and word not in stop_words]

word_set = set(word_set)

print(word_set)

word_map = {}
for i in word_set:
    word_map[str(i)] = 0

print(word_map)

for i in word_list:
    word_map[str(i)] += 1

print(word_map)