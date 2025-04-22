from keybert import KeyBERT
from typing import List
from sentence_transformers import SentenceTransformer
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus.common import thai_stopwords
import re

def is_valid_thai_word(word: str, min_len: int = 3) -> bool:
    if len(word) < min_len:
        return False
    thai_chars = re.findall(r'[\u0E00-\u0E7F]', word)
    return len(thai_chars) / len(word) >= 0.8

def is_good_keyword(keyword: str) -> bool:
    keyword = keyword.replace(" ", "")  # ตัด space ออกก่อน
    if len(keyword) < 3:
        return False
    if not all('\u0E00' <= c <= '\u0E7F' for c in keyword):
        return False
    # เช็คว่าคำลงท้ายด้วยพยัญชนะไทย ไม่ใช่ตัวสะกดแปลกๆ
    pattern = r"^[\u0E00-\u0E7F]+$"
    if not re.match(pattern, keyword):
        return False
    return True

class ThaiCustomTokenizer:
    def __init__(self, tokenizer_engine="attacut"):
        self.model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")
        self.kw_model = KeyBERT(self.model)
        self.tokenizer_engine = tokenizer_engine
        self.stop_words = self.get_preprocessed_stopwords()

    def clean_text(self, text: str) -> str:
        text = re.sub(r"[^\u0E00-\u0E7Fa-zA-Z0-9\s]", "", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def get_preprocessed_stopwords(self) -> List[str]:
        cleaned = [self.clean_text(w) for w in thai_stopwords()]
        tokenized = [token for stopword in cleaned for token in word_tokenize(stopword, engine=self.tokenizer_engine)]
        additional = ["ๆ", "ฯ", "และ", "หรือ", "ว่า", "แต่", "คือ", "ได้", "ให้", "โดย", "ก็", "เป็น", "ที่", "ของ", "กับ"]
        full_stopwords = set(tokenized + additional)
        full_stopwords = {w for w in full_stopwords if len(w) > 1}
        return list(full_stopwords)

    def chunk_tokens(self, tokens: List[str], max_ngram: int = 3) -> List[str]:
        chunks = []
        n = len(tokens)

        for size in range(1, max_ngram + 1):
            for i in range(n - size + 1):
                chunk = "".join(tokens[i:i+size])
                if is_valid_thai_word(chunk) and chunk not in self.stop_words:
                    chunks.append(chunk)

        return list(set(chunks))

    def preprocess_text(self, texts: List[str]) -> List[str]:
        cleaned = [self.clean_text(t) for t in texts if t and t.strip()]
        combined = " ".join(cleaned)
        tokens = word_tokenize(combined, engine=self.tokenizer_engine)
        tokens = [token.strip() for token in tokens if token.strip() and len(token.strip()) > 1]
        
        chunks = self.chunk_tokens(tokens, max_ngram=3)
        print("🔍 Chunked tokens:", chunks)
        return chunks

    def extract_keywords(self, texts: List[str], top_n: int = 5) -> List[str]:
        candidate_chunks = self.preprocess_text(texts)
        if not candidate_chunks:
            return []

        text_for_kw_model = " ".join(candidate_chunks)
        
        keywords = self.kw_model.extract_keywords(
            text_for_kw_model,
            candidates=candidate_chunks,
            keyphrase_ngram_range=(1, 3),   # 🛠
            stop_words=None,
            use_maxsum=True,
            nr_candidates=80,
            top_n=top_n,
        )

        print("🔍 Raw keywords:", keywords)

        filtered_keywords = []
        for kw, _ in keywords:
            if is_good_keyword(kw):
                filtered_keywords.append(kw)

        return list(dict.fromkeys(filtered_keywords))


