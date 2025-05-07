import streamlit as st
import requests
import json

# Groq API setup
GROQ_API_KEY = "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"  # Replace with your actual API key
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  # Correct API endpoint

def generate_summary(text):
    """Summarize input text using Groq API."""
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": f"Summarize this: {text}"}]
    }
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    response = requests.post(GROQ_API_URL, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Error generating summary")
    else:
        st.error(f"API Error: {response.status_code} - {response.text}")
        return "API request failed. Check console for details."

def generate_flashcards(summary):
    """Generate flashcards from summarized text using Groq API."""
    payload = {
        "model": "llama3-70b-8192",  # or another current model Groq supports

        "messages": [{"role": "user", "content": f"Create a list of Q&A flashcards from this summary:\n{summary}"}]
    }
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    response = requests.post(GROQ_API_URL, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Error generating flashcards")
    else:
        st.error(f"API Error: {response.status_code} - {response.text}")
        return "API request failed. Check console for details."

# Streamlit UI - Enhanced Design
st.set_page_config(page_title="AI Flashcard Generator", page_icon="📚", layout="wide")

# Custom CSS Styling
st.markdown(
    """
    <style>
        .title-text { text-align: center; font-size: 32px; font-weight: bold; color: #4A90E2; }
        .subtitle-text { text-align: center; font-size: 18px; color: #5F6368; }
        .stButton>button { width: 100%; border-radius: 8px; font-size: 18px; padding: 10px; background-color: #4CAF50; color: white; }
        .stTextArea textarea { border-radius: 10px; font-size: 16px; }
        .result-box { background-color: #E3F2FD; padding: 15px; border-radius: 8px; margin-bottom: 10px; border-left: 5px solid #1976D2; }
        .flashcard-box { background-color: #FFD700; padding: 15px; border-radius: 8px; margin-bottom: 10px; border-left: 5px solid #FF4500; }
        .container { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }
        .flashcard { width: 45%; padding: 15px; background-color: #FFF3CD; border-radius: 8px; border-left: 5px solid #FF9800; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<p class='title-text'>📚 AI Flashcard Generator</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>Enter text, and the AI will summarize it and generate flashcards!</p>", unsafe_allow_html=True)

# Initialize variables
summary = ""
flashcards = ""

# Input Section
user_input = st.text_area("Enter your text here:", height=200)
if st.button("Generate Flashcards"):
    if user_input.strip():
        with st.spinner("Generating summary..."):
            summary = generate_summary(user_input)
        
        with st.spinner("Generating flashcards..."):
            flashcards = generate_flashcards(summary)
    else:
        st.warning("Please enter some text!")

# Output Section
st.subheader("Summary")
st.markdown(f"<div class='result-box'>{summary if summary else 'Summary will appear here...'}</div>", unsafe_allow_html=True)

st.subheader("Generated Flashcards")
if flashcards:
    flashcard_list = flashcards.split("\n")  # Assuming flashcards are newline-separated
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    for card in flashcard_list:
        if card.strip():
            st.markdown(f"<div class='flashcard'>{card}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='flashcard-box'>Flashcards will appear here...</div>", unsafe_allow_html=True)
