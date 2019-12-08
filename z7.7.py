listaRijeci = []
rijec = input()
while rijec:
    listaRijeci.append(rijec)
    rijec = input()

sumaSlova = 0
for rijec in listaRijeci:
    sumaSlova += len(rijec)

prosjek = sumaSlova // len(listaRijeci)

for rijec in listaRijeci:
    if len(rijec) > prosjek:
        print(rijec)