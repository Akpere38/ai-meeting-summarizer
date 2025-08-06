# app.py

import streamlit as st
from utils.cleaner import clean_transcript
from utils.summarizer import summarize_text
from utils.sentiment import analyze_sentiment
from utils.action_extractor import extract_action_items
from docx import Document
import io

st.set_page_config(page_title="AI Meeting Summarizer", layout="wide")

st.title("🧠 AI-Powered Meeting Summarizer")
st.write("Upload your meeting transcript or paste it below. Get a concise summary, action points, and sentiment analysis.")

def read_docx(file): # Read .docx file and return text
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

def extract_text_from_vtt(vtt_content): # Extract text from VTT file content
    """
    Extract text from VTT content, removing timestamps and empty lines.
    """
    lines = vtt_content.splitlines()
    cleaned_lines = [
        line for line in lines
        if not line.strip().startswith("00:")
        and "-->" not in line
        and line.strip()
    ]
    return " ".join(cleaned_lines)


SAMPLE_TRANSCRIPT = """
John: Let's schedule the next review for Monday.
Sarah: I agree. Also, John will send the deck before Friday.
Mike: We should assign the final edits to Mary.
Anna: We also need to prepare the client summary.
"""



# Input options
uploaded_file = st.file_uploader("Upload Transcript (.txt, .docx, or .vtt)", type=["txt", "docx", "vtt"])
use_sample = st.checkbox("Use sample transcript")
default_text = "Paste transcript here..."
transcript_text = ""

if use_sample:
    transcript_text = SAMPLE_TRANSCRIPT

elif uploaded_file:
    if uploaded_file.name.endswith(".txt"):
        transcript_text = uploaded_file.read().decode("utf-8")
    elif uploaded_file.name.endswith(".docx"):
        transcript_text = read_docx(uploaded_file)
    elif uploaded_file.name.endswith(".vtt"):
        vtt_content = uploaded_file.read().decode("utf-8")
        transcript_text = extract_text_from_vtt(vtt_content)
    else:
        st.error("Unsupported file type. Please upload a .txt, .docx, or .vtt file.")
        transcript = None

else:
    transcript_text = st.text_area("Or paste the transcript", height=300, placeholder=default_text)



if st.button("Summarize Transcript"):
    if transcript_text.strip():
        with st.spinner("🧼 Cleaning transcript..."):
            cleaned = clean_transcript(transcript_text)

        with st.spinner("✂️ Summarizing..."):
            summary = summarize_text(cleaned)

        with st.spinner("🧭 Analyzing sentiment..."):
            sentiment = analyze_sentiment(cleaned)
        
        with st.spinner("🔍 Extracting action items..."):
            actions = extract_action_items(summary)

        st.subheader("📝 Action Items")
        if actions:
            for item in actions:
                st.markdown(f"- {item}")
        else:
            st.write("No clear action items detected.")

        st.subheader("📋 Summary")
        st.write(summary)

        st.subheader("😊 Sentiment")
        st.write(sentiment)

        # ✅ Optional: Add download buttons
        st.subheader("⬇️ Download Results")

        all_output = (
            "📋 Summary:\n" + summary + "\n\n" +
            "📝 Action Items:\n" + "\n".join(actions) + "\n\n" +
            "😊 Sentiment:\n" + sentiment
        )

        st.download_button(
            label="Download Full Report",
            data=all_output,
            file_name="meeting_summary_report.txt",
            mime="text/plain"
        )

else:
    st.info("Please upload or paste a transcript to begin.")
