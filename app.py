import streamlit as st
from ai_test import (
    summarize_notes,
    generate_mcqs,
    generate_exam_questions
)

st.set_page_config(page_title="AI Study Assistant", layout="centered")

st.title("📘 AI Study Assistant")
st.write("Paste your study notes below and generate summaries, MCQs, and exam questions.")

notes = st.text_area("📄 Paste your notes here", height=250)

if st.button("✨ Generate Output"):
    if notes.strip() == "":
        st.warning("Please paste some notes first.")
    else:
        with st.spinner("AI is thinking..."):
            summary = summarize_notes(notes)
            mcqs = generate_mcqs(notes)
            questions = generate_exam_questions(notes)

        st.subheader("📝 Summary")
        st.write(summary)

        st.subheader("🧠 MCQs")
        st.write(mcqs)

        st.subheader("🎓 Exam / Viva Questions")
        st.write(questions)
