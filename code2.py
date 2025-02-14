import streamlit as st
import google.generativeai as genai  # Google AI API
import os

# Set up Google AI API key
GOOGLE_API_KEY = "YOUR API_KEY"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Streamlit UI
st.title("AI Code Reviewer ⚛️")
st.write("Submit your code for AI-powered review.")

# Code input box
code = st.text_area("Paste your code here:", height=200)

# Function to analyze code using GoogleAI API
def analyze_code(code_snippet):
    """Sends code to GoogleAI API and returns analysis."""
    model = genai.GenerativeModel("models/gemini-2.0-flash-exp")  # Choose the appropriate GoogleAI model
    response = model.generate_content(f"Analyze only the code with all the programming languages and identify any bugs or improvements: \n\n{code_snippet}")
    return response.text  # Extract and return AI response

# Submit button
if st.button("Review Code "):
    if code.strip():
        st.write("🔍 Analyzing your code... Please wait.")
        try:
            feedback = analyze_code(code)
            st.subheader("📝 AI Feedback:")
            st.write(feedback)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some code before submitting.")
