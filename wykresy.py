from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('DANE.csv')
print(df.columns.tolist())

atrybuty = ['reception', 'age', 'price', 'action', 'adventure', 'casual', 'indie',
            'massively multiplayer', 'rpg', 'racing', 'simulation', 'sports', 'strategy']

wyniki = {}

for atrybut in atrybuty:
    wyniki[atrybut] = {}
    slow = {}
    X_train, X_test, y_train, y_test = train_test_split(df['NLTK'], df[atrybut], test_size=0.2, random_state=2137)

    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    svm = SVC()
    svm.fit(X_train_tfidf, y_train)
    predictions_svm = svm.predict(X_test_tfidf)

    slow["Dokladnosc"] = accuracy_score(y_test, predictions_svm)
    slow['Precyzja'] = precision_score(y_test, predictions_svm, average='weighted')
    slow["Czulosc"] = recall_score(y_test, predictions_svm, average='weighted')
    slow["F1-Score"] = f1_score(y_test, predictions_svm, average='weighted')


    # Compute confusion matrix
    cm = confusion_matrix(y_test, predictions_svm)

    # Save confusion matrix plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.xlabel('Predykowany')
    plt.ylabel('True')
    plt.title(f'Macierz pomyłek - {atrybut}')
    plt.savefig(f"MAC_POM_{atrybut}.png")
    plt.close()

    wyniki[atrybut] = slow

print(wyniki)
