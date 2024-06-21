import streamlit as st
import joblib
import re
import string
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.probability import FreqDist
import pickle

# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

STOPWORDS = stopwords.words('english')
STEMMER = PorterStemmer()
LEMMATIZER = WordNetLemmatizer()

def compress_repeating_char(word):
    return re.sub(r'(.)\1{2,}', r'\1', word)

def get_words(paragraph):
    words = [word.lower() for word in word_tokenize(paragraph)]
    words = [compress_repeating_char(w) for w in words]
    words = [word.lower() for word in words if word not in STOPWORDS]
    words = [word.lower() for word in words if word not in string.punctuation]
    words = [word.lower() for word in words if word.isalpha()]
    words = [word.lower() for word in words if word not in 'br']
    words = [STEMMER.stem(word) for word in words]
    words = [LEMMATIZER.lemmatize(word) for word in words]
    return words

st.title('NLP AOL')

# make an input paragraph
tweet = st.text_area('Enter a tweet:')

# make a dropdown to choose the model
modelType = st.selectbox('Choose a model:', ['Decision Tree', 'Linear Regression', 'Naive Bayes', 'Linear SVC', 'ADA Boost', 'Random Forest'])
model = None
# make a button for predicting hate speech
if st.button('Predict Hate Speech'):
    
    # load the model
    if modelType == 'Decision Tree':
        with open('decisionTree.pkl', 'rb') as f:
            model = pickle.load(f)
    elif modelType == 'Linear Regression':
        model = joblib.load('linear.pkl')
    elif modelType == 'Naive Bayes':
        model = joblib.load('naive.pkl')
    elif modelType == 'Linear SVC':
        model = joblib.load('linearsvc.pkl')
    elif modelType == 'ADA Boost':
        with open('adaboost.pkl', 'rb') as f:
            model = pickle.load(f)
    elif modelType == 'Random Forest':
        with open('rfc.pkl', 'rb') as f:
            model = pickle.load(f)
    else:
        st.write('Model not found')
    
    paragraph = get_words(tweet)
    
    # predict the hate speech
    prediction = model.classify(FreqDist(paragraph))
        
    
    # display the prediction
    st.write(f'The paragraph is a {prediction}')