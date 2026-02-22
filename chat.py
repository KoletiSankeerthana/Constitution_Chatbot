import os
from dotenv import load_dotenv

from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate

from models import Models

# Load env
load_dotenv()

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct database path
DB_PATH = os.path.join(BASE_DIR, "db", "chroma_langchain_db")

print("Using database:", DB_PATH)

# Initialize models
models = Models()
embeddings = models.embeddings_openai
llm = models.model_openai

# Load vector store with correct collection name
vector_store = Chroma(
    collection_name="constitution",
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

# Create retriever
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 6, "fetch_k": 20}
)

# Prompt
prompt = ChatPromptTemplate.from_template("""
You are an expert on the Indian Constitution.

Use the provided context to answer the question.

Context:
{context}

Question:
{question}

Answer clearly:
""")


def main():

    print("\nConstitution Chatbot Ready!")
    print("Type 'exit' to quit\n")

    while True:

        query = input("User: ")

        if query.lower() in ["exit", "quit", "q"]:
            break

        docs = retriever.invoke(query)

        print(f"[DEBUG] Retrieved {len(docs)} documents")

        if len(docs) == 0:
            print("Bot: Database is empty or not loaded properly.\n")
            continue

        context = "\n\n".join([doc.page_content for doc in docs])

        final_prompt = prompt.invoke({
            "context": context,
            "question": query
        })

        response = llm.invoke(final_prompt)

        print("\nBot:", response.content, "\n")


if __name__ == "__main__":
    main()