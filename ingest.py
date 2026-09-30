from pathlib import Path

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# Project paths
BASE_DIR = Path(__file__).resolve().parent

DOCUMENTS_DIR = BASE_DIR / "documents"
CHROMA_DIR = BASE_DIR / "chroma_db"

print("Project directory:", BASE_DIR)
print("Documents directory:", DOCUMENTS_DIR)
print("ChromaDB directory:", CHROMA_DIR)


# Load PDFs
print("\nLoading PDF documents...")

loader = PyPDFDirectoryLoader(
    str(DOCUMENTS_DIR)
)

documents = loader.load()

print(f"Loaded {len(documents)} pages from the documents.")


# Split documents
print("\nSplitting documents into chunks...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks.")


# Embeddings
print("\nLoading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded.")


# ChromaDB
print("\nCreating ChromaDB...")

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=str(CHROMA_DIR),
    collection_name="college_documents"
)

print("Documents stored in ChromaDB successfully!")


# Verify
count = vector_store._collection.count()

print(f"\nNumber of vectors stored: {count}")

print("\nIngestion completed successfully!")