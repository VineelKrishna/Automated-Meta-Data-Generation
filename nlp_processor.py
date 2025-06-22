import spacy
from keybert import KeyBERT
from transformers import pipeline
from sentence_transformers import SentenceTransformer
import en_core_web_sm

class NLPProcessor:

    def __init__(self):
        print("Loading spaCy model...")
        self.nlp = en_core_web_sm.load()

        print("Loading SentenceTransformer model from Hugging Face...")
        self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.kw_model = KeyBERT(model=self.sentence_model)

        print("Loading summarization model from Hugging Face...")
        self.summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=-1)

    def perform_ner(self, text):
        doc = self.nlp(text)
        return [(ent.label_, ent.text) for ent in doc.ents]

    def extract_keywords(self, text, top_n=5):
        return self.kw_model.extract_keywords(text, top_n=top_n)

    def summarize_text(self, text):
        short_text = text[:3000]
        summary = self.summarizer(short_text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        return summary
