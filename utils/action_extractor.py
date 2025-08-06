# # utils/action_extractor.py

# import re
# import nltk
# from nltk.tokenize import sent_tokenize
# import ssl
# import os
# import spacy
# nlp = spacy.load("en_core_web_sm")

# # Disable SSL verification for nltk data downloads
# ssl._create_default_https_context = ssl._create_unverified_context

# # Add relative path to nltk_data
# nltk_data_path = os.path.join(os.path.dirname(__file__), '..', 'nltk_data')
# nltk.data.path.append(nltk_data_path)

# # Explicitly tell NLTK where to look for resources
# nltk_data_path = os.path.join(os.path.dirname(__file__), '..', 'nltk_data')
# nltk.data.path.append(nltk_data_path)

# # Try to find 'punkt' tokenizer
# try:
#     nltk.data.find("tokenizers/punkt")
# except LookupError:
#     nltk.download("punkt", download_dir=nltk_data_path)


# ACTION_KEYWORDS = [
#     "assign", "send", "schedule", "follow up", "prepare", "review",
#     "let's", "we should", "I will", "I'll", "you need to", "remind", "we need to", "let’s", "please", "ensure", "make sure", 
#         "remember to", "you should", "don't forget", "we must", "action item:", "action point:", "action:", "task:", "to do:", "to-do:", "next step:", "next steps:", "follow up on", "check in on", "update on",
#     "get back to", "reach out to", "contact", "discuss with", "talk to", "meet with", "call", "email", "message", "notify", "inform",
#     "confirm", "verify", "validate", "review with", "send to", "share with", "distribute to", "assign to", "delegate to", "set deadline for", "set due date for", "complete by", "finish by", "wrap up", "close out",
#     "document", "record", "log", "note down", "write up", "summarize", "report back on", "provide update on", "give feedback on", "review progress on", "check status of", "follow through on", "follow up with", "reach out to", "coordinate with", "collaborate with", "work with", "partner with", "align with"
# ]

# def extract_action_items(text):
#     """
#     Extract possible action items from cleaned transcript or summary.
#     """
#     action_items = []
#     sentences = sent_tokenize(text)

#     for sentence in sentences:
#         for keyword in ACTION_KEYWORDS:
#             if re.search(rf"\b{re.escape(keyword)}\b", sentence, re.IGNORECASE):
#                 action_items.append(sentence.strip())
#                 break

#     return action_items


# # -------------------------------------------------------------------------------------------------------

# utils/action_extractor.py

import re
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

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
    Extract possible action items from cleaned transcript or summary using spaCy for sentence segmentation.
    """
    action_items = []
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]

    for sentence in sentences:
        for keyword in ACTION_KEYWORDS:
            if re.search(rf"\b{re.escape(keyword)}\b", sentence, re.IGNORECASE):
                action_items.append(sentence)
                break

    return action_items
