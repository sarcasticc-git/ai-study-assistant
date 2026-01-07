import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}


def call_llm(system_prompt, user_prompt):
    payload = {
        "model": "llama-3.1-70b-versatile",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(GROQ_URL, headers=HEADERS, json=payload)

    # Debug-friendly error
    if response.status_code != 200:
        raise Exception(f"Groq API Error {response.status_code}: {response.text}")

    return response.json()["choices"][0]["message"]["content"]


def summarize_notes(text):
    return call_llm(
        "You summarize study notes clearly and concisely.",
        f"Summarize the following notes:\n{text}"
    )


def generate_mcqs(text):
    return call_llm(
        "You create exam-oriented multiple choice questions.",
        f"Create 5 MCQs with 4 options and correct answers from:\n{text}"
    )


def generate_exam_questions(text):
    return call_llm(
        "You create university exam and viva questions.",
        f"Generate 5 important exam or viva questions from:\n{text}"
    )
