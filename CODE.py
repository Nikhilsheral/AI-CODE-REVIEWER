import streamlit as st
import google.generativeai as genai  # Google AI API

# Set up Google AI API key
GOOGLE_API_KEY = ""  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# System Instruction
sys_instruction = (
    "You are an expert code reviewer for all programming languages. "
    "Only analyze the code if input is provided. "
    "If no code is given, politely inform the user."
)

# Streamlit UI
st.title("🌐 AI Code Reviewer for All Languages")
st.write("Submit your code (any language) for AI-powered review.")

# Code input box
code = st.text_area("Paste your code here:", height=200)

# Function to analyze code using GoogleAI API
def analyze_code(code_snippet):
    """Sends code to GoogleAI API and returns analysis."""
    prompt = (
        f"{sys_instruction}\n\n"
        f"Analyze the following code written in any programming language. "
        f"Identify bugs, suggest improvements, and provide fixes if necessary:\n\n{code_snippet}"
    )
    response = genai.generate_text(prompt=prompt, model="models/gemini-2.0-flash-exp")
    return response.result  # Extract and return AI response

# Submit button
if st.button("🔍 Review Code"):
    if code.strip():
        st.write("Analyzing your code... Please wait ⏳")
        try:
            feedback = analyze_code(code)
            st.subheader("📝 AI Feedback:")
            st.markdown(feedback)  # Use markdown for better formatting
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter some code before submitting.")
