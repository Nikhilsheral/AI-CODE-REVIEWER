# AI Code Reviewer ⚛️  

This is a Streamlit-based web application that leverages Google's Generative AI to provide intelligent reviews of Python code. The app allows users to paste their code into a text area and get AI-powered feedback on potential bugs and improvements.

---

## Key Features  
- **AI-Powered Code Analysis**: Utilizes Google's Generative AI to analyze submitted Python code, identify potential bugs, and suggest improvements.  
- **User-Friendly Interface**: Built with Streamlit for a simple and intuitive UI.  
- **Dynamic Feedback**: Provides real-time analysis results directly on the web page.  

---

## How It Works  
1. Users paste their Python code into the provided text area.  
2. On clicking the "Review Code" button, the app sends the code to the Google Generative AI model for analysis.  
3. The AI reviews the code and returns detailed feedback, highlighting bugs and suggesting improvements.  
4. If no code is submitted, the app prompts the user to enter some code first.  

---

## Dependencies  
- **Streamlit**: For the web-based user interface.  
- **Google Generative AI (`google.generativeai`)**: For AI-powered code analysis.  

---

## Prerequisites  
- A Google API key with access to Google's Generative AI models.  
- Python environment with the required packages installed.  

---

## Installation  
1. **Clone the repository:**  
    ```bash
    git clone https://github.com/your-username/ai-code-reviewer.git
    cd ai-code-reviewer
    ```

2. **Install the required packages:**  
    ```bash
    pip install streamlit google-generativeai
    ```

3. **Configure the Google API Key:**  
   Replace `"YOUR API_KEY"` in the script with your actual Google API key.  

---

## Usage  
Run the Streamlit application using the following command:  
```bash
streamlit run app.py
```

This will launch a web interface where you can paste your Python code and click on "Review Code" to receive AI-generated feedback.

---

## Code Breakdown  
### Importing Required Libraries  
```python
import streamlit as st
import google.generativeai as genai
```

### API Configuration  
```python
GOOGLE_API_KEY = "YOUR API_KEY"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)
```
This sets up the Google Generative AI with the provided API key.  

### UI Design  
```python
st.title("AI Code Reviewer ⚛️")
st.write("Submit your code for AI-powered review.")
code = st.text_area("Paste your code here:", height=200)
```
This creates the web interface, including a text area for code input.  

### Code Analysis Function  
```python
def analyze_code(code_snippet):
    prompt = f"{sys_instruction}\n\nAnalyze the following code and identify any bugs or improvements:\n\n{code_snippet}"
    response = genai.generate_text(prompt=prompt, model="models/gemini-2.0-flash-exp")
    return response.result
```
This function sends the submitted code to the Google Generative AI model and returns the feedback.  

### Handling User Input  
```python
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
```
- When the "Review Code" button is clicked, the app checks if code is present.  
- If code is provided, it is sent for analysis, and the feedback is displayed.  
- If no code is provided, a warning message is shown.  
- Any errors during the analysis are caught and displayed as error messages.  

---

## Model Used  
The application uses the `gemini-2.0-flash-exp` model from Google Generative AI, known for its advanced natural language understanding and code analysis capabilities.  

---

## Improvements and Contributions  
- Feel free to contribute to the project by submitting pull requests or raising issues.  
- Suggestions for enhancing the UI or adding more features (e.g., support for other programming languages) are welcome.  

---

## License  
This project is licensed under the MIT License.  

---

## Acknowledgments  
- Thanks to Google for providing powerful Generative AI models.  
- Built using Streamlit, an amazing open-source framework for building web apps in Python.  

---

## Feedback and Support  
If you encounter any issues or have suggestions,feel freeto contact
mail id - nikhilsprofessional@gmail.com
linkedIn- nikhilsheral

---
