import os
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings


class Models:
    def __init__(self):

        groq_api_key = os.getenv("GROQ_API_KEY")

        if not groq_api_key:
            raise ValueError("Missing GROQ_API_KEY environment variable.")

        # Free HuggingFace embeddings
        self.embeddings_openai = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Updated Groq model (working)
        self.model_openai = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            groq_api_key=groq_api_key
        )


if __name__ == "__main__":
    models = Models()
    print("Groq models loaded successfully")