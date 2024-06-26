# -*- coding: utf-8 -*-
"""tweets_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V1JZdJ_ZMrZoFG5oAGoVGMm-wF01l-tN
"""

import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load training data
training_data = pd.read_csv('training_data.csv')

# Separate data based on labels
positive_samples = training_data[training_data['label'] == 1]
negative_samples = training_data[training_data['label'] == 0]

# Randomly select the same number of negative samples as positive samples
balanced_negative_samples = negative_samples.sample(n=len(positive_samples), random_state=42)

# Combine positive and balanced negative samples
balanced_training_data = pd.concat([positive_samples, balanced_negative_samples])

# Shuffle the balanced training data
balanced_training_data = balanced_training_data.sample(frac=1, random_state=42).reset_index(drop=True)

# Preprocessing
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenization and lowercasing
    tokens = [token for token in tokens if token.isalpha()]  # Remove non-alphabetic tokens
    tokens = [token for token in tokens if token not in stop_words]  # Remove stopwords
    tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Lemmatization
    return ' '.join(tokens)

balanced_training_data['clean_text'] = balanced_training_data['tweet'].apply(preprocess_text)

# Feature extraction
tfidf_vectorizer = TfidfVectorizer()
X = tfidf_vectorizer.fit_transform(balanced_training_data['clean_text'])
y = balanced_training_data['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
logistic_regression_model = LogisticRegression()
logistic_regression_model.fit(X_train, y_train)

# Model evaluation
y_pred = logistic_regression_model.predict(X_test)
print(classification_report(y_test, y_pred))







# Load testing data
testing_data = pd.read_csv('test_tweets.csv')

# Preprocessing for testing data
testing_data['clean_text'] = testing_data['tweet'].apply(preprocess_text)

# Transform testing data using the same TF-IDF vectorizer
X_test_new = tfidf_vectorizer.transform(testing_data['clean_text'])

# Predict sentiment for testing data
testing_data['sentiment'] = logistic_regression_model.predict(X_test_new)

# Print the testing data with predicted sentiments
print(testing_data)



num_unique_values = training_data.nunique()

# Print the number of unique values
print("Number of unique values in the dataset:")
print(num_unique_values)

# Get the frequency of each unique value
value_counts = training_data['label'].value_counts()

# Print the frequency of each unique value
print("\nFrequency of each unique value:")
print(value_counts)

