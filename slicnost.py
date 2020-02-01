unos = input()
recenica = "Programiranje ili racunarsko programiranje jeste vjestina pomocu koje korisnik stvara i izvrsava programske algoritme koristeci odredjene programske jezike da bi napravio racunarski program. Ono sadrzi elemente umjetnosti, nauke i matematike."

rijeci = recenica.lower().split()
for i in range(len(rijeci)):
    rijeci[i] = rijeci[i].strip(".,?!:;")

rez = dict()

for rijec in rijeci:
    brojac = 0
    slova_rijeci = list(rijec)
    slova_unosa = list(unos)
    for slovo in slova_unosa:
        if slovo in slova_rijeci:
            slova_rijeci.remove(slovo)
            brojac += 2
        else:
            brojac -= 1
    rez[rijec] = brojac - len(slova_rijeci)

maks_poklapanja = 0
for rijec in rez.keys():
    if rez[rijec] > maks_poklapanja:
        maks_poklapanja = rez[rijec]

for rijec in rez.keys():
    if rez[rijec] == maks_poklapanja:
        print(rijec)
