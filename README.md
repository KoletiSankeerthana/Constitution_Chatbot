
```markdown
# Constitution Chatbot (RAG-based AI Assistant)

An AI-powered chatbot that answers questions about the Constitution of India using Retrieval-Augmented Generation (RAG). This system retrieves relevant sections from the Constitution PDF and generates accurate answers using a Large Language Model.

---

## Features

- Ask questions about the Indian Constitution in natural language
- Retrieves relevant constitutional articles using semantic search
- Generates accurate answers using Groq LLM (Llama 3.3)
- Uses HuggingFace embeddings for semantic understanding
- Stores document vectors in ChromaDB
- Displays source page numbers for verification
- Fully local vector database (no cloud dependency for storage)

---

## Tech Stack

- Python
- LangChain
- Groq API (LLM inference)
- HuggingFace Embeddings
- ChromaDB (Vector Database)
- PyPDFLoader (Document loading)

---

## Project Structure

```

Constitution_ChatBot/
│
├── chat.py              # Main chatbot interface
├── ingest.py            # Document ingestion and vector storage
├── models.py            # Model and embedding configuration
├── data/
│   └── Constitution.pdf # Constitution document
├── db/                  # Vector database (auto-generated)
├── .gitignore
└── README.md

````

---

## How It Works

1. The Constitution PDF is loaded and split into chunks
2. Each chunk is converted into embeddings using HuggingFace
3. Embeddings are stored in ChromaDB
4. When a user asks a question:
   - Relevant chunks are retrieved
   - Context is sent to Groq LLM
   - Answer is generated based on retrieved content

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/KoletiSankeerthana/Constitution_Chatbot.git
cd Constitution_Chatbot
````

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install langchain langchain-community langchain-groq chromadb python-dotenv sentence-transformers pypdf
```

---

## Setup API Key

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from:
[https://console.groq.com/](https://console.groq.com/)

---

## Run Document Ingestion

```bash
python ingest.py
```

This creates the vector database.

---

## Run Chatbot

```bash
python chat.py
```

Example:

```
User: What is Article 21?

Bot: Article 21 guarantees protection of life and personal liberty...

---

