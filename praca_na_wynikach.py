import json

with open('wynikiFIN.json', 'r') as f:
    wyniki = json.load(f)

atrybuty = ['reception', 'age', 'price', 'action', 'adventure', 'casual', 'indie',
            'massively multiplayer', 'rpg', 'racing', 'simulation', 'sports', 'strategy']

teksty = ['SpaCy', 'Gensim', 'NLTK']
metody = ['BOW', 'TF-IDF']
kryteria_jakosci = ['Dokladnosc', 'Precyzja', 'Czulosc', 'F1-Score']

slownik_najlepszych = {}

for atrybut in atrybuty:
    slownik_najlepszych[atrybut] = {}
    for kryterium in kryteria_jakosci:
        slownik_najlepszych[atrybut][kryterium] = {
            'tekst': '',
            'metoda': '',
            'klasyfikator': '',
            'wynik': 0
        }

    for tekst in teksty:
        for metoda in metody:
            for kryterium in kryteria_jakosci:
                for klasyfikator, wynik in wyniki[atrybut][tekst][metoda][kryterium].items():
                    if wynik > slownik_najlepszych[atrybut][kryterium]['wynik']:
                        slownik_najlepszych[atrybut][kryterium] = {
                            'tekst': tekst,
                            'metoda': metoda,
                            'klasyfikator': klasyfikator,
                            'wynik': wynik
                        }

print("Słownik najlepszych wyników:")
print(slownik_najlepszych)
for atrybut in atrybuty:
    print(atrybut)
    for kryterium in kryteria_jakosci:
        print(kryterium)
        print(slownik_najlepszych[atrybut][kryterium])

# with open('slownik_najlepszych.json', 'w') as f:
#     json.dump(slownik_najlepszych, f, indent=2)