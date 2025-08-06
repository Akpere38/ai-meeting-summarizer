# utils/summarizer.py

from transformers import pipeline

# summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


def summarize_text(text, max_chunk=1024):
    """
    Summarize long text by chunking.
    """
    chunks = []
    while len(text) > max_chunk:
        split_at = text[:max_chunk].rfind(".")
        chunks.append(text[:split_at+1])
        text = text[split_at+1:]
    chunks.append(text)

    summary = ""
    for chunk in chunks:
        result = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
        summary += result[0]['summary_text'] + " "

    return summary.strip()
