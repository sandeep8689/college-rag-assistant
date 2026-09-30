import streamlit as st
import requests


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="College AI Assistant",
    page_icon="🎓"
)


# -----------------------------
# Title
# -----------------------------

st.title("🎓 College AI Assistant")

st.write(
    "Ask questions about academic regulations, "
    "placements, and internships."
)


# -----------------------------
# Question input
# -----------------------------

question = st.text_input(
    "Enter your question:"
)


# -----------------------------
# Ask button
# -----------------------------

if st.button("Ask AI"):

    if not question:

        st.warning(
            "Please enter a question."
        )

    else:

        try:

            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={
                    "question": question
                }
            )

            response.raise_for_status()

            result = response.json()

            st.subheader("Answer")

            st.write(
                result["answer"]
            )

        except requests.exceptions.RequestException:

            st.error(
                "Could not connect to the FastAPI backend. "
                "Make sure the backend is running."
            )