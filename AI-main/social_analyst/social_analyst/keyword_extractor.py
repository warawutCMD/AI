from keybert import KeyBERT
from typing import List
from sentence_transformers import SentenceTransformer
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus.common import thai_stopwords
import re

class ThaiKeywordExtractor:
    def __init__(self, tokenizer_engine="attacut"):
        self.model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")
        self.kw_model = KeyBERT(self.model)
        self.tokenizer_engine = tokenizer_engine
        self.stop_words = self.get_preprocessed_stopwords()

    def clean_text(self, text: str) -> str:
        text = re.sub(r"[^\u0E00-\u0E7Fa-zA-Z0-9\s]", "", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def preprocess_text(self, texts: List[str]) -> str:
        cleaned = [self.clean_text(t) for t in texts if t and t.strip()]
        if not cleaned:
            return ""

        combined = " ".join(cleaned)
        tokens = word_tokenize(combined, engine=self.tokenizer_engine)

        # 💥 กรอง token เฉพาะที่ยาว > 1 ตัวอักษร และไม่ใช่ stopword
        tokens = [token.strip() for token in tokens if token.strip() and len(token.strip()) > 1 and token not in self.stop_words]

        final_text = " ".join(tokens)
        print("🔍 Clean tokens:", tokens)
        print("🔍 Combined clean text:", final_text)
        return final_text


    def get_preprocessed_stopwords(self) -> List[str]:
        cleaned = [self.clean_text(w) for w in thai_stopwords()]
        tokenized = [token for stopword in cleaned for token in word_tokenize(stopword, engine=self.tokenizer_engine)]
        # เพิ่ม stopwords custom
        additional = ["ๆ", "ฯ", "และ", "หรือ", "ว่า", "แต่", "คือ", "ได้", "ให้", "โดย", "ก็", "เป็น", "ที่", "ของ", "กับ"]
        full_stopwords = set(tokenized + additional)
        # กรองเอาคำที่ยาวกว่า 1 ตัวอักษรเท่านั้น
        full_stopwords = {w for w in full_stopwords if len(w) > 1}
        return list(full_stopwords)

    def extract_keywords(self, texts: List[str], top_n: int = 5) -> List[str]:
        combined_text = self.preprocess_text(texts)
        if not combined_text:
            return []

        keywords = self.kw_model.extract_keywords(
            combined_text,
            keyphrase_ngram_range=(1, 3),
            stop_words=self.stop_words,
            use_maxsum=True,
            nr_candidates=60,
            top_n=top_n,
        )

        print("🔍 Raw keywords:", keywords)
        filtered_keywords = [kw[0] for kw in keywords if kw[0] not in self.stop_words]
        return list(dict.fromkeys(filtered_keywords))
