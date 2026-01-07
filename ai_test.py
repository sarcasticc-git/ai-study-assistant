import os
import requests

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()[0]["generated_text"]

def summarize_notes(text):
    return query({
        "inputs": f"Summarize the following notes:\n{text}"
    })

def generate_mcqs(text):
    return query({
        "inputs": f"Create 5 MCQs with options and answers from the following notes:\n{text}"
    })

def generate_exam_questions(text):
    return query({
        "inputs": f"Generate 5 important exam or viva questions from the following notes:\n{text}"
    })
