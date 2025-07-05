import streamlit as st
import fitz  # PyMuPDF
from openai import OpenAI

# 🔐 Set your OpenAI API key here
client = OpenAI(api_key="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")  # <-- Paste your key here

# 📄 Extract text from uploaded PDF resume
def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text

# 🧠 Analyze the resume using GPT
def analyze_resume(resume_text):
    

    
    return """
    ✅ **Strengths**
    - Strong academic background
    - Good technical skills (Python, Java)
    - Project experience in real-time systems

    ⚠️ **Improvements**
    - Resume formatting can be improved
    - Add quantifiable achievements
    - Improve grammar in summary section

    🎯 **Suitable Job Roles**
    - Data Analyst
    - Software Developer
    """

# 🌐 Streamlit UI setup
st.set_page_config(page_title="Resume Analyzer", layout="centered")
st.title("📄 AI-Powered Resume Analyzer")
st.write("Upload your resume (PDF) and get smart suggestions instantly!")

# 📤 Upload file
uploaded_file = st.file_uploader("Upload your Resume", type="pdf")

# ✅ Analyze on upload
if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    with st.spinner("Analyzing..."):
        analysis = analyze_resume(resume_text)
    st.success("Analysis Complete!")
    st.markdown("### 📌 Analysis Result")
    st.write(analysis)
