from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

import tempfile
import os
import fitz  # PyMuPDF for PDF handling
from docx import Document
from transformers import pipeline

app = Flask(__name__)
CORS(app)
summarizer = pipeline("summarization")

def extract_text_from_pdf(file_path):
    pdf_document = fitz.open(file_path)
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    file_type = file.filename.split('.')[-1].lower()

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file.read())
        temp_file_path = temp_file.name

    try:
        if file_type == 'pdf':
            text = extract_text_from_pdf(temp_file_path)
        elif file_type == 'docx':
            text = extract_text_from_docx(temp_file_path)
        else:
            return jsonify({"error": "Unsupported file type"}), 400

        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
        response = {"summary": summary[0]['summary_text']}
        return jsonify(response)

    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
