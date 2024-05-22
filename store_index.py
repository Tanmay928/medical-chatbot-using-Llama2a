from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
import pinecone
from dotenv import load_dotenv
import os


load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
index_name = os.environ.get('index_name')

# print(PINECONE_API_KEY)
# print(index_name)

extracted_data = load_pdf(data="data/")

text_chunks = text_split(extracted_data)
print("length of the chunk:",len(text_chunks))

embeddings = download_hugging_face_embeddings()


os.environ['PINECONE_API_KEY'] = '2c8650bc-84f5-4999-8b8d-045d8ef905aa'

docsearch = PineconeVectorStore.from_texts(
    [t.page_content for t in text_chunks],
    embeddings,
    index_name = index_name
)