import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"


def call_llm(system_prompt, user_prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.4
    }

    response = requests.post(GROQ_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def summarize_notes(text):
    return call_llm(
        "You summarize study notes clearly and concisely.",
        f"Summarize the following notes:\n{text}"
    )


def generate_mcqs(text):
    return call_llm(
        "You create exam-oriented multiple choice questions.",
        f"""Create 5 MCQs from the following notes.
Each MCQ should have 4 options (A, B, C, D) and mention the correct answer clearly.

{text}
"""
    )


def generate_exam_questions(text):
    return call_llm(
        "You create university exam and viva questions.",
        f"Generate 5 important exam or viva questions from the following notes:\n{text}"
    )
