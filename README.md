# 🎓 College AI Assistant – RAG Based Question Answering System

A Retrieval-Augmented Generation (RAG) based AI assistant that allows students to ask questions about college-related documents such as academic regulations and internship guidelines.

The application retrieves relevant information from uploaded PDF documents and uses an LLM to generate answers based on the retrieved content.

---

## 📌 Project Overview

The **College AI Assistant** is designed to provide students with quick and accurate answers from college documents without manually searching through lengthy PDF files.

Instead of directly asking an AI model to answer questions from its general knowledge, this system first searches the college documents for relevant information and then provides the retrieved context to the AI model.

This approach is called **Retrieval-Augmented Generation (RAG)**.

### Example

A student can ask:

> What is the minimum attendance required for students?

The system searches the uploaded college documents and generates an answer based on the relevant content.

Example response:

> The minimum attendance required is 75%.

---

# 🚀 Features

- 📄 PDF document processing
- 🔎 Semantic document search
- 🤖 AI-powered question answering
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 Multiple college documents supported
- 💾 Vector database using ChromaDB
- 🔤 Hugging Face sentence embeddings
- ⚡ Groq LLM for fast response generation
- 🌐 FastAPI backend
- 🎨 Streamlit frontend
- 📝 Question and answer history stored in JSON
- 🔐 API keys managed using environment variables

---

# 🏗️ System Architecture

The application follows the following pipeline:

```text
                 User
                  │
                  ▼
        ┌──────────────────┐
        │ Streamlit Frontend│
        └─────────┬────────┘
                  │
                  ▼
        ┌──────────────────┐
        │   FastAPI Backend │
        └─────────┬────────┘
                  │
                  ▼
        ┌──────────────────┐
        │   RAG Pipeline    │
        └─────────┬────────┘
                  │
                  ▼
        ┌──────────────────┐
        │ HuggingFace       │
        │ Embedding Model   │
        └─────────┬────────┘
                  │
                  ▼
        ┌──────────────────┐
        │    ChromaDB       │
        │  Vector Database  │
        └─────────┬────────┘
                  │
                  ▼
        Relevant Documents
                  │
                  ▼
        ┌──────────────────┐
        │   Groq LLM        │
        └─────────┬────────┘
                  │
                  ▼
             AI Answer
                  │
                  ▼
             User
