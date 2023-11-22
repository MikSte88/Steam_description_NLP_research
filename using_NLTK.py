import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Inicjalizacja lematyzatora
lemmatizer = WordNetLemmatizer()

# Pobieranie stopwords
stop_words = set(stopwords.words('english'))

# Wczytywanie danych z pliku CSV
df = pd.read_csv(r'DANE.csv')

# Tokenizacja, usuwanie stopwords i lematyzacja dla każdego opisu
df['BOW_NLTK'] = df['description'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in nltk.word_tokenize(x) if word.lower() not in stop_words]))

df.to_csv('DANE.csv', index=False)

