# utils/action_extractor.py

import re
import nltk
from nltk.tokenize import sent_tokenize
import ssl

# Disable SSL verification for nltk data downloads
ssl._create_default_https_context = ssl._create_unverified_context

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
# nltk.download('punkt_tab') # "punkt_tab" is a newer, more accurate version of the same tokenizer.

ACTION_KEYWORDS = [
    "assign", "send", "schedule", "follow up", "prepare", "review",
    "let's", "we should", "I will", "I'll", "you need to", "remind", "we need to", "let’s", "please", "ensure", "make sure", 
        "remember to", "you should", "don't forget", "we must", "action item:", "action point:", "action:", "task:", "to do:", "to-do:", "next step:", "next steps:", "follow up on", "check in on", "update on",
    "get back to", "reach out to", "contact", "discuss with", "talk to", "meet with", "call", "email", "message", "notify", "inform",
    "confirm", "verify", "validate", "review with", "send to", "share with", "distribute to", "assign to", "delegate to", "set deadline for", "set due date for", "complete by", "finish by", "wrap up", "close out",
    "document", "record", "log", "note down", "write up", "summarize", "report back on", "provide update on", "give feedback on", "review progress on", "check status of", "follow through on", "follow up with", "reach out to", "coordinate with", "collaborate with", "work with", "partner with", "align with"
]

def extract_action_items(text):
    """
    Extract possible action items from cleaned transcript or summary.
    """
    action_items = []
    sentences = sent_tokenize(text)

    for sentence in sentences:
        for keyword in ACTION_KEYWORDS:
            if re.search(rf"\b{re.escape(keyword)}\b", sentence, re.IGNORECASE):
                action_items.append(sentence.strip())
                break

    return action_items
