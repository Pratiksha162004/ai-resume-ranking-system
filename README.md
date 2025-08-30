# AI-Powered Resume Analyzer  

**AI-Powered Resume Analyzer**, a cutting-edge application designed to mimic the expertise of an HR professional! This tool leverages the power of **Google Generative AI** to analyze resumes, evaluate job compatibility, and offer actionable insights for career enhancement.  

---

📄 AI Resume Analyzer

An AI-powered web application built with Streamlit that analyzes resumes and matches them against a given job description. The tool extracts text from PDF resumes, processes it using NLP techniques, and provides a similarity score to rank candidates.

🚀 Features

Upload multiple resumes in PDF format

Enter a job description

Extracts and processes text using NLP

Generates a similarity score between resume & job description

Displays ranked results

🛠️ Tech Stack

Python 3

Streamlit – Web framework

pdfplumber – Extract text from PDFs

scikit-learn – TF-IDF Vectorizer & Cosine Similarity

NLTK – Natural Language Processing

Pandas & NumPy – Data handling

📂 Project Structure
ai-resume-analyzer/
│── app.py                # Main Streamlit app
│── requirements.txt      # Required dependencies
│── README.md             # Project documentation
│── sample_resumes/       # (Optional) Store test resumes

⚙️ Installation

Clone this repository:

git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

📊 Example Output

Upload resumes and paste a job description.

The app will calculate similarity scores.

Example result:

Resume_1.pdf → 82% match
Resume_2.pdf → 65% match
Resume_3.pdf → 40% match

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

📜 License

This project is licensed under the MIT License.

