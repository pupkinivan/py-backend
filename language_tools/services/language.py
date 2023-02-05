from nltk import word_tokenize, SnowballStemmer
from typing import List

stemmer = SnowballStemmer(language="spanish")

def tokenize_text(text: str) -> List[str]:
    return word_tokenize(text=text, language="spanish")

def extract_stems(text: str) -> List[str]:
    return [
        stemmer.stem(word)
        for word in tokenize_text(text)
    ]
