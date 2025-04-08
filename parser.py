import fitz  # PyMuPDF
import docx
import os

def extract_text_from_pdf(path):
    text = ''
    with fitz.open(path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return '\n'.join([para.text for para in doc.paragraphs])

def parse_resume(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    else:
        raise Exception("Unsupported file format")
