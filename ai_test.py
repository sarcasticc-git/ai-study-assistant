import ollama

def summarize_notes(text):
    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {"role": "system", "content": "You summarize study notes clearly and concisely."},
            {"role": "user", "content": f"Summarize the following notes:\n{text}"}
        ]
    )
    return response["message"]["content"]


def generate_mcqs(text):
    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {"role": "system", "content": "You create exam-oriented multiple choice questions."},
            {
                "role": "user",
                "content": (
                    "Create 5 MCQs from the following notes.\n"
                    "Each MCQ should have 4 options (A, B, C, D) and clearly mention the correct answer.\n\n"
                    f"{text}"
                ),
            },
        ]
    )
    return response["message"]["content"]


def generate_exam_questions(text):
    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {"role": "system", "content": "You create university exam and viva questions."},
            {
                "role": "user",
                "content": (
                    "Generate 5 important exam or viva questions from the following notes:\n\n"
                    f"{text}"
                ),
            },
        ]
    )
    return response["message"]["content"]


print("Paste your notes (press Enter, then Ctrl+Z, then Enter on Windows):")
notes = ""
while True:
    try:
        line = input()
        notes += line + "\n"
    except EOFError:
        break

print("\n🔹 SUMMARY 🔹\n")
print(summarize_notes(notes))

print("\n🔹 MCQs 🔹\n")
print(generate_mcqs(notes))

print("\n🔹 EXAM / VIVA QUESTIONS 🔹\n")
print(generate_exam_questions(notes))
