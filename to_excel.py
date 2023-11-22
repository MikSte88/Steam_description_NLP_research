import json
import pandas as pd
import matplotlib.pyplot as plt

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

# Create a DataFrame from the nested dictionary
data = []
for atrybut in atrybuty:
    for kryterium in kryteria_jakosci:
        row = {
            'atrybut': atrybut,
            'kryterium': kryterium,
            'tekst': slownik_najlepszych[atrybut][kryterium]['tekst'],
            'metoda': slownik_najlepszych[atrybut][kryterium]['metoda'],
            'klasyfikator': slownik_najlepszych[atrybut][kryterium]['klasyfikator'],
            'wynik': slownik_najlepszych[atrybut][kryterium]['wynik']
        }
        data.append(row)

df = pd.DataFrame(data)

combination_counts = {}
# Iterate over the DataFrame rows
for index, row in df.iterrows():
    combination = f"{row['tekst']}+{row['metoda']}+{row['klasyfikator']}"

    # Increment the count for the combination or initialize it to 1 if it doesn't exist
    combination_counts[combination] = combination_counts.get(combination, 0) + 1

# Print the combinations and their counts
for combination, count in combination_counts.items():
    print(f"{combination}: {count}")

# Prepare data for the pie chart
combinations = list(combination_counts.keys())
counts = list(combination_counts.values())

# Create a pie chart
plt.pie(counts, labels=combinations, autopct='%1.1f%%')

# Add a title
plt.title('Udział kombinacji narzędzi w najlepszych wynikach dla wszystkich')

# Display the chart
plt.show()