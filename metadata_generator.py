from extractor import extract_text
from nlp_processor import NLPProcessor

def generate_metadata(file_path):
    print("Extracting text from file...")
    text = extract_text(file_path)

    processor = NLPProcessor()
    
    print("Generating metadata...")
    entities = processor.perform_ner(text)
    keywords = processor.extract_keywords(text)
    summary = processor.summarize_text(text)

    metadata = {
        "Entities": entities,
        "Keywords": keywords,
        "Summary": summary
    }
    return metadata
