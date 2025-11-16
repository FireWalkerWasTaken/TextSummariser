import streamlit as st

st.title('Text Summarization')

InputText = st.text_area("Enter text to Summarize")

st.subheader("Summary")

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import re
import math
from nltk.tokenize import word_tokenize, sent_tokenize
import contractions
from nltk.tokenize import RegexpTokenizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import nltk

nltk.download('punkt')
nltk.download('stopwords')

InputTextSentences = sent_tokenize(InputText)

WordsInSentenceList = [word_tokenize(sentence.lower()) for sentence in InputTextSentences]

NoStopWordsSentences = [word for sentence in WordsInSentenceList for word in sentence if word not in stopwords.words('english')]

NoStopWordsSentencesJoined = " ".join(NoStopWordsSentences).split(' . ')

RegexTokenizer = RegexpTokenizer(r'\w+')

NoPunctuationSentences = [RegexTokenizer.tokenize(sentence) for sentence in NoStopWordsSentencesJoined]

ProcessedData = [" ".join(sentence) for sentence in NoPunctuationSentences]

Vectorizer = TfidfVectorizer()
VectorizedDataMatrix = Vectorizer.fit_transform(ProcessedData)

similarityMatrix = cosine_similarity(VectorizedDataMatrix)
similarities = []
for index, similarity in enumerate(similarityMatrix):
    similarities.append({'similarityID': index, 'similarity': np.sum(similarity[1]) / len(similarityMatrix)})

sortedSimilarities = sorted(similarities, key = lambda x: x['similarity'], reverse=True)

SummaryLength = math.floor(len(InputTextSentences) / 6)

summary = []
for sentenceID in range(SummaryLength):
    targetSentenceID = sortedSimilarities[sentenceID]['similarityID']
    summary.append(InputTextSentences[targetSentenceID])

st.write(" ".join(summary))
