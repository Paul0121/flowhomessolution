import streamlit as st
from transformers import pipeline

# Set a local directory for caching the model to prevent re-downloading issues
MODEL_NAME = "sshleifer/distilbart-cnn-12-6"

summarizer = pipeline("summarization", model=MODEL_NAME, cache_dir="./models")

# Streamlit App
st.title("Conversation Summarizer")

# Text input area for pasting conversation
conversation = st.text_area("Paste your conversation here:")

if st.button("Summarize"):
    if conversation.strip():
        summary = summarizer(conversation, max_length=130, min_length=30, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please paste a conversation before summarizing.")
