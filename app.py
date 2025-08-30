import streamlit as st
import pdfplumber
import docx
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ------------ Extract Text Functions ----------------
def extract_text_from_pdf(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        st.error(f"PDF वाचताना Error: {e}")
    return text

def extract_text_from_docx(file):
    text = ""
    try:
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        st.error(f"DOCX वाचताना Error: {e}")
    return text

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip().lower()

# ------------ Matching Function ----------------
def calculate_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(similarity[0][0] * 100, 2)

# ------------ Streamlit UI ----------------
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📝", layout="wide")
st.title("📝 AI Resume Analyzer")
st.write("Upload resumes आणि एक Job Description देऊन similarity check करा.")

jd_text = st.text_area("📌 Job Description टाका", height=200)

uploaded_files = st.file_uploader("📂 Resumes Upload करा (PDF किंवा DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("🚀 Analyze") and jd_text and uploaded_files:
    jd_clean = clean_text(jd_text)

    results = []
    for file in uploaded_files:
        if file.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(file)
        elif file.name.endswith(".docx"):
            resume_text = extract_text_from_docx(file)
        else:
            continue

        resume_clean = clean_text(resume_text)
        score = calculate_similarity(resume_clean, jd_clean)
        results.append((file.name, score))

    # Sort by score (highest first)
    results = sorted(results, key=lambda x: x[1], reverse=True)

    st.subheader("📊 Resume Ranking Results")
    for name, score in results:
        st.write(f"**{name}** → Similarity: **{score}%**")
