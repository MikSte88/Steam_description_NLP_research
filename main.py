import pandas as pd
import json
from funkcje import *
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv(r'DANE.csv')
print(df.columns.tolist())

# Wiek, gatunek i odbiór gry:
szukane_atrybuty = ['reception', 'age', 'price', 'action', 'adventure', 'casual', 'indie',
                    'massively multiplayer', 'rpg', 'racing', 'simulation', 'sports', 'strategy', ]

sprocesowane_teksty = ['SpaCy', 'Gensim', 'NLTK']

wyniki = {}
# Dla każdego atrybutu
for atrybut in szukane_atrybuty:
    wyniki[atrybut] = {}
    # Do każdej próbki tekstu
    for tekst in sprocesowane_teksty:

        slownik = {}
        #Patrzymy na sprocesowane teksty
        X_train, X_test, y_train, y_test = train_test_split(df[tekst], df[atrybut], test_size=0.2,random_state=2137)

        # BoW
        vectorizer = CountVectorizer()
        X_train_bow = vectorizer.fit_transform(X_train)
        X_test_bow = vectorizer.transform(X_test)


        print(f" Dla Bag Of Words predyktując {atrybut} w oparciu o {tekst}")
        slownik["BOW"] = porownywarka_klasyfiaktorow(X_train_bow, X_test_bow, y_train, y_test)

        # TF-IDF
        vectorizer = TfidfVectorizer()
        X_train_tfidf = vectorizer.fit_transform(X_train)
        X_test_tfidf = vectorizer.transform(X_test)

        print(f" Dla TF-IDF predyktując {atrybut} w oparciu o {tekst}")
        slownik["TF-IDF"] = porownywarka_klasyfiaktorow(X_train_tfidf, X_test_tfidf, y_train, y_test)


        wyniki[atrybut][tekst] = slownik
        with open('wyniki.json', 'w') as f:
            json.dump(wyniki, f, indent=3)


with open('wynikiFIN.json', 'w') as f:
    json.dump(wyniki, f, indent=3)







