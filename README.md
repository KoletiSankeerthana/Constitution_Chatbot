
# Constitution Chatbot (RAG-based AI Assistant)

An AI-powered chatbot that answers questions about the Constitution of India using Retrieval-Augmented Generation (RAG). It retrieves relevant constitutional articles from a PDF and generates accurate answers using a Large Language Model.

---

## Features

* Ask questions about the Indian Constitution in natural language
* Retrieves relevant constitutional articles using semantic search
* Generates accurate answers using Groq LLM (Llama 3.3)
* Uses HuggingFace embeddings for semantic understanding
* Stores document vectors in ChromaDB
* Displays source page numbers for verification
* Fully local vector database

---

## Tech Stack

* Python
* LangChain
* Groq API (LLM inference)
* HuggingFace Embeddings
* ChromaDB (Vector Database)
* PyPDFLoader

---

## Project Structure

```
Constitution_ChatBot/
│
├── chat.py              # Chatbot interface
├── ingest.py            # Document ingestion and vector storage
├── models.py            # Model and embedding configuration
├── data/
│   └── Constitution.pdf # Constitution document
├── db/                  # Vector database (auto-generated)
├── .gitignore
└── README.md
```

---

## How It Works

1. Loads Constitution PDF
2. Splits text into chunks
3. Converts chunks into embeddings
4. Stores embeddings in ChromaDB
5. Retrieves relevant context for user query
6. Generates answer using Groq LLM

---

---

## Demo

Example interaction with the chatbot:

<img width="955" height="561" alt="image" src="https://github.com/user-attachments/assets/4793f24d-c430-4e99-bdc0-1e6d396fe865" />

---

## Installation

Clone repository:

```
git clone https://github.com/KoletiSankeerthana/Constitution_Chatbot.git
cd Constitution_Chatbot
```

Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```
pip install langchain langchain-community langchain-groq chromadb python-dotenv sentence-transformers pypdf
```

---

## Setup API Key

Create `.env` file in the project root:

```
GROQ_API_KEY=your_api_key_here
```

Get your API key from:
[https://console.groq.com/](https://console.groq.com/)

---

## Run Ingestion

```
python ingest.py
```

---

## Run Chatbot

```
python chat.py
```

---

