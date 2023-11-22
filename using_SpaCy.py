import pandas as pd
import spacy


nlp = spacy.load("en_core_web_sm")
DFCalosc = pd.read_csv(r'Przygotowane_dane.csv')
def przetworz_tekst_stop_i_lemmatyzcja(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)


DFCalosc['processed_description'] = DFCalosc['description'].apply(przetworz_tekst_stop_i_lemmatyzcja)
DFCalosc.to_csv('SpaCy_przygotowane.csv', index=False)


