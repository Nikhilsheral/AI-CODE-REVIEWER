import streamlit as st
import google.generativeai as genai  # Google AI API

# Set up Google AI API key
GOOGLE_API_KEY = "YOUR API_KEY"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# System Instruction
sys_instruction = "Only review the code if you get input, otherwise politely inform the user."

# Streamlit UI
st.title("AI Code Reviewer ⚛️")
st.write("Submit your code for AI-powered review.")

# Code input box
code = st.text_area("Paste your code here:", height=200)

# Function to analyze code using GoogleAI API
def analyze_code(code_snippet):
    """Sends code to GoogleAI API and returns analysis."""
    prompt = f"{sys_instruction}\n\nAnalyze the following code and identify any bugs or improvements:\n\n{code_snippet}"
    response = genai.generate_text(prompt=prompt, model="models/gemini-2.0-flash-exp")
    return response.result  # Extract and return AI response

# Submit button
if st.button("Review Code"):
    if code.strip():
        st.write("🔍 Analyzing your code... Please wait.")
        try:
            feedback = analyze_code(code)
            st.subheader("📝 AI Feedback:")
            st.write(feedback)
        except Exception as e:
            st.error(f"Error: {"You need to only input the code "}")
    else:
        st.warning("Please enter some code before submitting.")
