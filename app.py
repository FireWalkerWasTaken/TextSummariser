import math
import nltk
import numpy as np
import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@st.cache_resource
def load_nltk():
    for pkg in ("punkt", "punkt_tab", "stopwords"):
        nltk.download(pkg, quiet=True)
    return set(stopwords.words("english"))


STOP_WORDS = load_nltk()
tokenizer = RegexpTokenizer(r"\w+")


def clean(sentence):
    words = tokenizer.tokenize(sentence.lower())
    return " ".join(w for w in words if w not in STOP_WORDS)


def summarize(text, ratio=1 / 6):
    sentences = sent_tokenize(text)
    if len(sentences) < 2:
        return text

    processed = [clean(s) for s in sentences]   # same length as sentences
    if not any(processed):
        return text

    tfidf = TfidfVectorizer().fit_transform(processed)
    sim = cosine_similarity(tfidf)

    # score = average similarity to all other sentences
    scores = (sim.sum(axis=1) - 1) / (len(sentences) - 1)

    k = max(1, math.floor(len(sentences) * ratio))
    top = sorted(np.argsort(scores)[::-1][:k])   # keep original order
    return " ".join(sentences[i] for i in top)


st.title("Text Summarization")
input_text = st.text_area("Enter text to Summarize")
ratio = st.slider("Summary length (fraction of original)", 0.1, 0.5, 1 / 6)

st.subheader("Summary")
if input_text.strip():
    st.write(summarize(input_text, ratio))
