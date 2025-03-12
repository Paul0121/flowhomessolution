import streamlit as st
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization")

# Streamlit App
st.title("Conversation Summarizer")

# Text input area for pasting conversation
conversation = st.text_area("Paste your conversation here:")

if st.button("Summarize"):
    if conversation.strip():
        # Use the summarization model
        summary = summarizer(conversation, max_length=130, min_length=30, do_sample=False)
        
        # Extract and display the summary text
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please paste a conversation before summarizing.")

# Run this app with: `streamlit run your_script.py`
