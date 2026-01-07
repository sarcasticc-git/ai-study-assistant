import os
from groq import Groq

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_notes(text):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You summarize study notes clearly and concisely."},
            {"role": "user", "content": f"Summarize the following notes:\n{text}"}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content


def generate_mcqs(text):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You create exam-oriented multiple choice questions."},
            {"role": "user", "content": f"""
Create 5 MCQs from the following notes.
Each MCQ should have 4 options (A, B, C, D) and clearly mention the correct answer.

{text}
"""}
        ],
        temperature=0.4
    )
    return response.choices[0].message.content


def generate_exam_questions(text):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You create university exam and viva questions."},
            {"role": "user", "content": f"""
Generate 5 important exam or viva questions from the following notes:

{text}
"""}
        ],
        temperature=0.4
    )
    return response.choices[0].message.content
