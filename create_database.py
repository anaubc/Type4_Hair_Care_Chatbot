from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os, shutil

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

CHROMA_PATH = "chroma"
DATA_PATH = "data"

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    return loader.load()

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    return chunks

def save_to_chroma(chunks):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    embeddings = OpenAIEmbeddings(openai_api_key=API_KEY)
    db = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_PATH)
    print(f"Saved {len(chunks)} to {CHROMA_PATH}.")

def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)

if __name__ == "__main__":
    generate_data_store()
