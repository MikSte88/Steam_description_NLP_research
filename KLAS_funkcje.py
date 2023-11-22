from datetime import datetime


def polacz_snippet_i_descr(rzad):
    try:
        snippet =str(rzad['desc_snippet'])
    except TypeError:
        snippet = ""
    try:
        descr = str(rzad['game_description'])
    except TypeError:
        descr = ""
    return "".join([snippet," ", descr])

def redaguj_cene(rzad):
    tekst = str(rzad['original_price'])
    try:
        znak = tekst[0]
        # Obsluga wiekszosci
        if znak == "$":
            cena = float(tekst[1: 5])
            if cena == 0.00:
                return "F2P"
            elif cena < 20.00:
                return "small"
            elif cena < 50.00:
                return "AA"
            else:
                return "AAA"
        # Obsluga zbugowanych gier activison
        elif znak == "1":
            return "AAA"
        # Obsluga F2P
        else:
            return "F2P"
    except IndexError:
        return "F2P"

def postrzeganie_gry(rzad):
    try:
        tekst = rzad['all_reviews'].lower()
        for i in range(len(tekst)):
            if tekst[i: i+5] == "mixed":
                return "mixed"
            elif tekst[i: i+8] == "positive":
                return "positive"
            elif tekst[i: i+8] == "negative":
                return "negative"
        return "usun"
    except AttributeError:
        return "usun"


def wiek_gry(rzad):
    s = str(rzad['release_date'])
    try:
        t = datetime.strptime(s, "%b %d, %Y")
        # Usuwanie wtedy jeszcze nie wydanych
        rok = int(str(t)[0:4])
        if rok < 2000:
            return "RETRO"
        elif rok < 2010:
            return "OLD"
        elif rok <2017:
            return "YOUNG"
        else:
            return "NEW"
    except ValueError:
        return "usun"

def eksportuj_gatunki(rzad, dozwolone_gatunki):
    gatunki = str(rzad['genre']).split(",")
    wyjscie = ""
    for gatunek in gatunki:
        if gatunek in dozwolone_gatunki:
            wyjscie += gatunek + ","
    if wyjscie == []:
        return "usun"
    else:
        return wyjscie[0:len(wyjscie)-1]

