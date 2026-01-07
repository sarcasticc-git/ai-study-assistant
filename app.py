import streamlit as st
import subprocess

st.set_page_config(page_title="AI Study Assistant", layout="centered")

st.title("📘 AI Study Assistant")
st.write("Paste your study notes below and generate summaries, MCQs, and exam questions.")

notes = st.text_area("📄 Paste your notes here", height=250)

def run_ai(notes_text):
    # Add Windows EOF (Ctrl+Z) so ai_test.py stops waiting
    notes_with_eof = notes_text + "\n\x1a\n"

    process = subprocess.Popen(
        ["python", "ai_test.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output, error = process.communicate(input=notes_with_eof)
    return output if output else error


if st.button("✨ Generate Output"):
    if notes.strip() == "":
        st.warning("Please paste some notes first.")
    else:
        with st.spinner("AI is thinking..."):
            result = run_ai(notes)
        st.subheader("📤 Output")
        st.code(result)
