# 🧠 AI-Powered Flashcard Generator with Summarization and Chatbot

This project is an intelligent learning assistant that uses Large Language Models (LLMs) like LLaMA-3 or Mixtral (via Groq API) to summarize input content and automatically generate flashcards. It also includes a chatbot for interactive Q&A, built using Retrieval-Augmented Generation (RAG) with ChromaDB for document retrieval. The frontend is built with Streamlit and everything runs in a Docker container for easy deployment.

---

## 🚀 Features

- Automatic content summarization using LLMs
- Flashcard generation from summaries (Q&A format)
- RAG-based chatbot to answer user queries
- ChromaDB for vector storage and retrieval
- Streamlit frontend for ease of use
- Dockerized deployment for consistency across systems

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- LLaMA-3 / Mixtral via Groq API
- ChromaDB
- Docker

---

## 📦 Installation

**Using Docker:**

```bash
git clone https://github.com/your-username/flashcard-llm-project.git
cd flashcard-llm-project
docker build -t flashcard-generator .
docker run -p 8501:8501 flashcard-generator
