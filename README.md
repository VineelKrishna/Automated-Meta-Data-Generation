# Automated Metadata Generation System

This project is an automated system designed to enhance document discoverability, classification, and analysis by producing scalable, consistent, and semantically rich metadata from various document types.

---

## 🚀 Key Features

* **Multi-Format Content Extraction**: Extracts text from `PDF`, `DOCX`, `TXT`, and image (`JPG`, `PNG`) files.
* **OCR Integration**: Automatically uses Optical Character Recognition (OCR) for scanned PDFs and images to extract text.
* **Rich Metadata Generation**: Produces a structured set of metadata including:

  * **Summary**: A generated summary of the content.
  * **Keyphrases**: The most important phrases and terms.
  * **Named Entities**: Recognizes entities like people, organizations, and locations (`PERSON`, `ORG`, `GPE`).
* **Web Interface**: An intuitive web application built with Streamlit for easy document upload and metadata viewing.

---

## 📂 Project Structure

```
mars_project/
│
├── app.py                   # Streamlit Web App
├── extractor.py             # Document extraction module
├── nlp_processor.py         # NLP processing module
├── metadata_generator.py    # Metadata generation logic
├── requirements.txt         # Python dependencies
├── models/                  
│   ├── spacy_model/en_core_web_sm/
│   ├── summarizer_model/
│   └── sentence_transformer_model/
│
└── README.md                # Project Documentation
```

---

## 🛠️ Setup and Installation

### 1️⃣ Prerequisites

You must have **Google's Tesseract-OCR engine** installed on your system. The Python `pytesseract` library is just a wrapper for it.

* **Windows**: Download and install from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).

  * After installation, add Tesseract installation path (e.g., `C:\Program Files\Tesseract-OCR`) to your system `PATH` variable.
* **macOS**: `brew install tesseract`
* **Linux (Debian/Ubuntu)**: `sudo apt-get install tesseract-ocr`

---

### 2️⃣ Clone the Repository

```bash
git clone <repository-url>
cd mars_project
```

---

### 3️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv metadata_env
```

Activate environment:

* **Windows:**

```bash
metadata_env\Scripts\activate
```

* **Linux/Mac:**

```bash
source metadata_env/bin/activate
```

---

### 4️⃣ Install Dependencies

Install all required Python packages using:

```bash
pip install -r requirements.txt
```

**⚠ No internet download of models is required. All models are pre-downloaded in `models/` folder.**

---

## ▶️ How to Run the Application

Activate your virtual environment and run:

```bash
streamlit run app.py
```

The web app will open in your browser. You can now upload a document and generate its metadata.

---

## 💡 Technologies Used

* Python 3.10+
* Streamlit
* spaCy (Named Entity Recognition)
* HuggingFace Transformers (Summarization)
* KeyBERT (Keyword Extraction)
* pdfplumber, python-docx, pytesseract (Document Extraction)

---

## 🙏 Acknowledgements

* HuggingFace
* spaCy
* KeyBERT
* Streamlit
* pdfplumber, pytesseract

---