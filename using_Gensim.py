import pandas as pd
from gensim.parsing.preprocessing import remove_stopwords
from gensim.utils import simple_preprocess

# Wczytanie danych
df = pd.read_csv('DANE.csv')

# Funkcja do przetwarzania tekstu
def preprocess_text(text):
    # Usunięcie stop words
    text = remove_stopwords(text)
    # Tokenizacja tekstu
    tokens = simple_preprocess(text, min_len=3)  # Min_len=3 odrzuci krótkie słowa
    # Połączenie tokenów w jedną string
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

# Stworzenie nowej kolumny "BOW_Gensim" na podstawie kolumny "description"
df['BOW_Gensim'] = df['description'].apply(preprocess_text)
df.to_csv('DANE.csv', index=False)
