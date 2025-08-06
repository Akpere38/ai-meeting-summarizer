# utils/sentiment.py

# utils/sentiment.py

# utils/sentiment.py

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

# Define the path relative to the project
VADER_LEXICON_PATH = os.path.join("utils", "vader_data", "vader_lexicon.txt")

class CustomSentimentIntensityAnalyzer(SentimentIntensityAnalyzer):
    def __init__(self):
        super().__init__(lexicon_file=VADER_LEXICON_PATH)

# Try to initialize the analyzer
try:
    sia = CustomSentimentIntensityAnalyzer()
except Exception as e:
    print("⚠️ Failed to load custom VADER lexicon:", e)
    sia = None


def analyze_sentiment(text):
    """
    Return sentiment score using local VADER lexicon.
    """
    if not sia:
        return "Sentiment analysis unavailable."

    scores = sia.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "😊 Positive"
    elif compound <= -0.05:
        sentiment = "😠 Negative"
    else:
        sentiment = "😐 Neutral"

    return f"{sentiment} (compound score: {compound:.2f})"


