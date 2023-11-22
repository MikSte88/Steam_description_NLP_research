def oczyszcz(plik, nazwa_docelowa, problem):
    dane = ""
    n_dane = ""

    with open(plik, "r", encoding="utf-8") as r:
        dane = repr(r.read())

    i = 0
    while i < len(dane)-7:
        if dane[i:i+2] == '\\n' and dane[i+2:i+7] != 'https':
            print(dane[i+2:i+7])
            n_dane += ""
            i += 2
        else:
            n_dane += dane[i]
            i += 1
        print(f"{i} z {len(dane)}")

    n_dane.replace(problem,'')

    with open(nazwa_docelowa, "w", encoding="utf-8") as w:
        w.write(n_dane)
