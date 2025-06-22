import spacy
from keybert import KeyBERT
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer
import en_core_web_sm

class NLPProcessor:

    def __init__(self, summarizer_path="./models/summarizer_model", sentence_model_path="./models/sentence_transformer_model"):
        print("Loading spaCy model...")
        self.nlp = en_core_web_sm.load()

        print("Loading KeyBERT model...")
        self.sentence_model = SentenceTransformer(sentence_model_path)
        self.kw_model = KeyBERT(model=self.sentence_model)

        print("Loading summarization model...")
        tokenizer = AutoTokenizer.from_pretrained(summarizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(summarizer_path)
        self.summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

    def perform_ner(self, text):
        doc = self.nlp(text)
        return [(ent.label_, ent.text) for ent in doc.ents]

    def extract_keywords(self, text, top_n=5):
        return self.kw_model.extract_keywords(text, top_n=top_n)

    def summarize_text(self, text):
        short_text = text[:3000]
        summary = self.summarizer(short_text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        return summary