import os
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI

class Models:
    def __init__(self):
        # Fetching environment variables with validation
        azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
        azure_endpoint = os.getenv("AZURE_OPENAI_EMBEDDINGS_ENDPOINT")
        azure_api_version = os.getenv("AZURE_OPENAI_EMBEDDINGS_API_VERSION", "2023-12-01-preview")
        azure_chat_deployment = os.getenv("AZURE_OPENAI_API_DEPLOYMENT_NAME")

        # Ensure all required variables are set
        if not azure_api_key:
            raise ValueError("Missing AZURE_OPENAI_API_KEY environment variable.")
        if not azure_endpoint:
            raise ValueError("Missing AZURE_OPENAI_EMBEDDINGS_ENDPOINT environment variable.")
        if not azure_api_version:
            raise ValueError("Missing AZURE_OPENAI_EMBEDDINGS_API_VERSION environment variable.")
        if not azure_chat_deployment:
            raise ValueError("Missing AZURE_OPENAI_API_DEPLOYMENT_NAME environment variable.")

        # Initialize Ollama models
        self.embeddings_ollama = OllamaEmbeddings(model="mxbai-embed-large")
        self.model_ollama = ChatOllama(model="phi3:mini", temperature=0)

        # Initialize Azure OpenAI Embeddings
        self.embeddings_openai = AzureOpenAIEmbeddings(
            model="text-embedding-3-large",
            dimensions=1536,
            azure_endpoint=azure_endpoint,
            api_key=azure_api_key,
            api_version=azure_api_version,  # Ensure it's explicitly provided
        )

        # Initialize Azure OpenAI Chat Model
        self.model_openai = AzureChatOpenAI(
            azure_deployment=azure_chat_deployment,
            api_version=azure_api_version,
            api_key=azure_api_key,  # Ensure API key is explicitly set
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )

# Run a test initialization to verify
if __name__ == "__main__":
    try:
        models = Models()
        print("Model initialization successful!")
    except Exception as e:
        print(f"Error initializing models: {e}")
