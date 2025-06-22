import streamlit as st
import os
import tempfile
import json

from metadata_generator import generate_metadata

st.set_page_config(page_title="Metadata Generator", page_icon="📄", layout="centered")

st.title("📄 Automated Metadata Generator")

uploaded_file = st.file_uploader("Upload your document (PDF, DOCX, TXT, Image)", type=['pdf', 'docx', 'txt', 'jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    st.write("Processing your file...")

    metadata = generate_metadata(tmp_file_path)

    st.success("Metadata Generated!")

    st.subheader("Summary")
    st.write(metadata['Summary'])

    st.subheader("Keywords")
    st.write([kw[0] for kw in metadata['Keywords']])

    st.subheader("Named Entities")
    st.write(metadata['Entities'])

    # Optionally, download metadata as JSON
    json_str = json.dumps(metadata, indent=4)
    st.download_button("Download Metadata as JSON", json_str, file_name="metadata.json")

    os.remove(tmp_file_path)
