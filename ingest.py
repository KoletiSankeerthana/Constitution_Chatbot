import os
from dotenv import load_dotenv
from uuid import uuid4

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from models import Models

# =====================================
# Load environment variables
# =====================================
load_dotenv()

# =====================================
# Initialize models
# =====================================
models = Models()
embeddings = models.embeddings_openai

# =====================================
# Configuration
# =====================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "data")
PERSIST_DIRECTORY = os.path.join(BASE_DIR, "db", "chroma_langchain_db")

# Improved chunking for Constitution articles
CHUNK_SIZE = 1800
CHUNK_OVERLAP = 200

# =====================================
# Ensure db folder exists
# =====================================
os.makedirs(PERSIST_DIRECTORY, exist_ok=True)

# =====================================
# Initialize vector store
# =====================================
vector_store = Chroma(
    collection_name="constitution",
    embedding_function=embeddings,
    persist_directory=PERSIST_DIRECTORY
)

# =====================================
# Function to ingest file
# =====================================
def ingest_file(file_path):

    if not file_path.lower().endswith(".pdf"):
        print(f"Skipping non-PDF file: {file_path}")
        return

    print(f"\nLoading file: {file_path}")

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    # FIXED: text_splitter must be INSIDE function
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=[
            "\n\nArticle ",
            "\nArticle ",
            "\n\n",
            "\n",
            ". ",
            " "
        ]
    )

    split_documents = text_splitter.split_documents(documents)

    print(f"Split into {len(split_documents)} chunks")

    ids = [str(uuid4()) for _ in range(len(split_documents))]

    vector_store.add_documents(
        documents=split_documents,
        ids=ids
    )

    print("Stored successfully in ChromaDB")


# =====================================
# Main function
# =====================================
def main():

    print("Using data folder:", DATA_FOLDER)
    print("Using db folder:", PERSIST_DIRECTORY)

    if not os.path.exists(DATA_FOLDER):
        print("ERROR: data folder not found")
        return

    files = os.listdir(DATA_FOLDER)

    if not files:
        print("ERROR: no files in data folder")
        return

    for filename in files:

        # Skip already processed files
        if filename.startswith("_"):
            continue

        file_path = os.path.join(DATA_FOLDER, filename)

        ingest_file(file_path)

        # Rename file after processing
        new_filename = "_" + filename
        new_file_path = os.path.join(DATA_FOLDER, new_filename)

        os.rename(file_path, new_file_path)

        print("Marked as processed:", new_filename)


# =====================================
# Run
# =====================================
if __name__ == "__main__":
    main()