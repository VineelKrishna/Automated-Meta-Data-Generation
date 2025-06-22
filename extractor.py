import os
import pdfplumber
import pytesseract
from PIL import Image
import docx

def extract_text(path):
    ext = os.path.splitext(path)[-1].lower()
    if ext == '.pdf':
        return extract_text_pdf_with_ocr(path)
    elif ext == '.docx':
        return extract_text_docx(path)
    elif ext == '.txt':
        return extract_text_txt(path)
    elif ext in ['.jpg', '.jpeg', '.png']:
        return extract_text_image(path)
    else:
        raise ValueError(f'Unsupported file format: {ext}')

def extract_text_pdf_with_ocr(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
            else:
                page_image = page.to_image(resolution=300)
                ocr_text = pytesseract.image_to_string(page_image.original)
                text += ocr_text + "\n"
    return text

def extract_text_docx(path):
    doc = docx.Document(path)
    return '\n'.join([p.text for p in doc.paragraphs])

def extract_text_txt(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text_image(path):
    image = Image.open(path)
    return pytesseract.image_to_string(image)
