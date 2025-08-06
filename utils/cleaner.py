# utils/cleaner.py

import re

def clean_transcript(text):
    """
    Remove speaker tags, timestamps, and extra whitespace.
    """
    # Remove timestamps like [00:12:34] or (00:12)
    text = re.sub(r"\[?\(?\d{1,2}:\d{2}(?::\d{2})?\)?\]?", "", text)

    # Remove speaker names like JOHN:, Mary - or Speaker 1:
    text = re.sub(r"(?i)(speaker\s*\d+|[A-Z][a-z]+)(:|-)", "", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text
