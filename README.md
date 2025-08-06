
# 🧠 AI-Powered Meeting Summarizer

An intelligent, lightweight NLP app that processes meeting transcripts and generates concise **bullet-point summaries**, **action items**, and **sentiment analysis**—helping teams save time and stay aligned.

Built with **Streamlit**, **transformers**, and **spaCy/NLTK**, this app is designed to enhance productivity by turning long meeting transcripts into clear, actionable insights.

---

## 🔍 Features

* ✨ **Abstractive Meeting Summarization** using pre-trained transformer models (`facebook/bart-large-cnn` or `google/pegasus-xsum`)
* ✅ **Action Item Extraction** via rule-based NLP using `nltk` and curated action keyword patterns
* 😊 **Sentiment Analysis** using either `VADER` or transformer-based sentiment models
* 📁 Upload support for `.txt` transcript files
* 🧩 Modular and extensible codebase

---

## 📸 App Demo

[Live Streamlit App](#) – *(insert when deployed)*
![App Screenshot](./assets/app_screenshot.png) *(optional)*

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **NLP Models**: HuggingFace Transformers (`BART`, `PEGASUS`)
* **Tokenization & Action Parsing**: `nltk`, `spaCy`
* **Sentiment**: `VADER` or HuggingFace sentiment models
* **Language**: Python 3.10+

---

## 🚀 How It Works

1. **User Uploads Transcript** → Accepts raw `.txt` files.
2. **Summarizer Module** → Generates a concise summary using a transformer model.
3. **Action Extractor** → Scans text for actionable phrases using regex and rule-based heuristics.
4. **Sentiment Module** → Analyzes the general tone (positive, neutral, negative).
5. **Streamlit UI** → Presents results with clear, user-friendly visuals.

---

## 🧪 Installation

```bash
git clone https://github.com/yourusername/meeting-summarizer.git
cd meeting-summarizer
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Make sure `punkt` is available for NLTK:

```python
import nltk
nltk.download("punkt")
```

---

## 📂 Project Structure

```
meeting-summarizer/
│
├── app.py                    # Streamlit main app
├── summarizer.py            # Transformer summarization logic
├── sentiment.py             # Sentiment analysis logic
├── action_extractor.py      # Rule-based action extraction (your script)
├── utils/                   # Preprocessing, helpers
├── requirements.txt
└── README.md
```

---

## 📈 Example Use Case

**Scenario**: After a long Zoom team meeting, upload the transcript into the app.
**Output**:

* 📋 A summary you can paste into Slack or Notion.
* ✅ Action items for your team to track.
* 😀 An overview of team sentiment.

---

## 🧠 Future Enhancements

* Multi-language support (via mBART)
* Audio-to-transcript support using Whisper
* Named entity tagging (NER)
* GPT-4 Turbo-based summarization (optional)

---

## 📚 Credits

* [Hugging Face Transformers](https://huggingface.co/)
* [NLTK](https://www.nltk.org/)
* [spaCy](https://spacy.io/)
* [VADER Sentiment](https://github.com/cjhutto/vaderSentiment)
* [Streamlit](https://streamlit.io/)

---

## 🧳 For Recruiters

This is a **portfolio project** showcasing my skills in:

* **NLP** and **transformer-based summarization**
* **Rule-based and hybrid AI techniques**
* **Rapid prototyping** using Streamlit
* **Clean code** and **modular design**

