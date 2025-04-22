from keybert import KeyBERT
from typing import List

class KeywordExtractor:
    def __init__(self):
        self.model = KeyBERT(model='all-MiniLM-L6-v2')  # เร็วและเบา

    def extract_keywords(self, texts: List[str], top_n: int = 5) -> List[str]:
        """
        รับ list ของคอมเมนต์ และรวมมาวิเคราะห์ keyword เด่น
        """
        combined_text = " ".join(texts)
        keywords = self.model.extract_keywords(
            combined_text,
            keyphrase_ngram_range=(1, 2),
            stop_words='english',
            top_n=top_n
        )
        return [kw[0] for kw in keywords]
