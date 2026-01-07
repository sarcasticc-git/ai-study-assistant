import os
import sys
from groq_sdk import Groq


# Initialize Groq client using Streamlit Secrets
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def call_llm(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.5,
    )
    return response.choices[0].message.content


def summarize_notes(text):
    return call_llm(
        "You summarize study notes clearly and concisely.",
        f"Summarize the following notes:\n{text}"
    )


def generate_mcqs(text):
    return call_llm(
        "You create exam-oriented multiple choice questions.",
        (
            "Create 5 MCQs from the following notes.\n"
            "Each MCQ should have 4 options (A, B, C, D) "
            "and clearly mention the correct answer.\n\n"
            f"{text}"
        ),
    )


def generate_exam_questions(text):
    return call_llm(
        "You create university exam and viva questions.",
        (
            "Generate 5 important exam or viva questions "
            "from the following notes:\n\n"
            f"{text}"
        ),
    )


# -------- INPUT HANDLING (Streamlit compatible) --------
def read_notes():
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return ""


notes = read_notes().strip()

if not notes:
    print("No input provided.")
    sys.exit(0)


print("\n=== SUMMARY ===\n")
print(summarize_notes(notes))

print("\n=== MCQs ===\n")
print(generate_mcqs(notes))

print("\n=== EXAM / VIVA QUESTIONS ===\n")
print(generate_exam_questions(notes))
