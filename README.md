<div align="center">

# 📝 Text Summariser

**Turn long articles into the few sentences that matter, instantly, right in your browser.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-TF--IDF-F7931E?logo=scikitlearn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-154F5B)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

## ✨ Overview

**Text Summariser** is a lightweight, **extractive** summarization app built with Streamlit. Paste in any article, pick how short you want the summary, and get back the most representative sentences, in their original order so the result still reads naturally.

No API keys, no GPU, no model downloads. Just classic NLP that you can read and understand in a few minutes.

<!-- Add a screenshot or GIF of the app here:
<p align="center"><img src="assets/demo.png" width="700" alt="Text Summariser demo"></p>
-->

## 🚀 Features

- ⚡ **Instant summaries** with no training and no external APIs
- 🎚️ **Adjustable length**: choose between 10% and 50% of the original text
- 🧭 **Original order preserved**, so summaries read like real prose
- 🧹 **Smart preprocessing**: tokenization, lowercasing and stop-word removal
- 🛡️ **Graceful fallbacks**: very short or empty-after-cleaning inputs are returned unchanged
- 🖥️ **Clean web UI** powered by Streamlit

## 🧠 How It Works

```
 Raw text ──► Sentence split ──► Clean & remove stop words ──► TF-IDF vectors
                                                                     │
 Summary ◄── Restore original order ◄── Pick top-k sentences ◄── Cosine similarity
```

1. **Split** the text into sentences with NLTK's `sent_tokenize`.
2. **Clean** each sentence: lowercase it, keep only word characters, and drop English stop words.
3. **Vectorize** every sentence with scikit-learn's `TfidfVectorizer`.
4. **Compare** all sentences with pairwise **cosine similarity**.
5. **Score** each sentence by its average similarity to every *other* sentence. Sentences that overlap most with the rest of the text are the most central to it.
6. **Select** the top `k = max(1, floor(n × ratio))` sentences, where `n` is the number of sentences.
7. **Reorder** the picks to match their position in the original text and join them.

> This is *extractive* summarization: it selects existing sentences instead of generating new ones, so the output never contains made-up facts.

## 🛠️ Tech Stack

| Purpose | Library |
|---|---|
| Web app | [Streamlit](https://streamlit.io/) |
| Sentence & word tokenization, stop words | [NLTK](https://www.nltk.org/) |
| TF-IDF & cosine similarity | [scikit-learn](https://scikit-learn.org/) |
| Numerics | [NumPy](https://numpy.org/) |

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/FireWalkerWasTaken/TextSummariser.git
cd TextSummariser

# 2. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install streamlit nltk numpy scikit-learn
```

The required NLTK data (`punkt`, `punkt_tab`, `stopwords`) is downloaded automatically the first time the app runs.

## ▶️ Usage

```bash
streamlit run app.py
```

> Replace `app.py` with the name of your main file if it's different.

Then open the local URL Streamlit prints (usually `http://localhost:8501`) and:

1. Paste your text into the box.
2. Drag the slider to set the summary length.
3. Read your summary.

### Use it as a Python function

```python
from app import summarize

text = open("article.txt").read()
print(summarize(text, ratio=0.2))   # keep roughly the top 20% of sentences
```

## 🎛️ Configuration

| Option | Where | Default | Description |
|---|---|---|---|
| `ratio` | UI slider / function argument | `1/6` | Fraction of sentences to keep (slider range: 0.1 to 0.5) |

## ⚠️ Limitations

- **Extractive only**: it can't paraphrase, merge ideas, or write new sentences.
- **Bag-of-words matching**: TF-IDF ignores word order and meaning, so synonyms and subtle context can be missed.
- **English only**: stop words and tokenization are set up for English.
- **Best on longer text**: with fewer than two sentences, the input is returned as is.

## 🗺️ Roadmap

- [ ] Compare against TextRank and embedding-based scoring
- [ ] Evaluate summaries with ROUGE
- [ ] Upload `.txt` / `.pdf` files
- [ ] Multi-language support
- [ ] Deploy on Streamlit Community Cloud

## 🤝 Contributing

Ideas and pull requests are welcome. Fork the repo, create a branch, make your changes and open a PR. For larger changes, open an issue first to discuss what you'd like to change.


## 👤 Author

**Lakshay**
[LinkedIn](https://linkedin.com/in/lakshayghai) · [GitHub](https://github.com/FireWalkerWasTaken)

---

<div align="center">

If you found this useful, consider giving the repo a ⭐

</div>
