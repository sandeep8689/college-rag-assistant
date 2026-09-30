from fastapi import FastAPI
from pydantic import BaseModel

from backend.rag import ask_question

import json
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

CHROMA_DIR = BASE_DIR / "chroma_db"

QA_FILE = CHROMA_DIR / "qa_history.json"


app = FastAPI(
    title="College AI Assistant",
    description="RAG-based AI assistant for college documents",
    version="1.0"
)


class Question(BaseModel):
    question: str


@app.get("/")
def home():

    return {
        "message": "College AI Assistant API is running"
    }


def save_question_answer(question, answer):

    if QA_FILE.exists():

        with open(QA_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)

    else:

        history = []


    record = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "answer": answer
    }


    history.append(record)


    with open(QA_FILE, "w", encoding="utf-8") as file:

        json.dump(
            history,
            file,
            indent=4,
            ensure_ascii=False
        )


@app.post("/ask")
def ask(data: Question):

    question = data.question

    answer = ask_question(question)

    save_question_answer(
        question,
        answer
    )

    return {
        "question": question,
        "answer": answer
    }