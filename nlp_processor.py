import spacy
from keybert import KeyBERT
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer
import torch

class NLPProcessor:

    def __init__(self):
        print("Loading spaCy model...")
        self.nlp = spacy.load("en_core_web_sm")

        print("Loading KeyBERT model...")
        device = 'cpu'
        self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2', device=device)
        self.kw_model = KeyBERT(model=self.sentence_model)

        print("Loading summarization model...")
        summarizer_model = "sshleifer/distilbart-cnn-12-6"
        tokenizer = AutoTokenizer.from_pretrained(summarizer_model)
        model = AutoModelForSeq2SeqLM.from_pretrained(summarizer_model)
        self.summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

    def perform_ner(self, text):
        doc = self.nlp(text)
        return [(ent.label_, ent.text) for ent in doc.ents]

    def extract_keywords(self, text, top_n=5):
        return self.kw_model.extract_keywords(text, top_n=top_n)

    def summarize_text(self, text):
        short_text = text[:3000]
        summary = self.summarizer(short_text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        return summary
