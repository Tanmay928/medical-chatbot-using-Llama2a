from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
import pinecone
from dotenv import load_dotenv
import os


load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

print(PINECONE_API_KEY)