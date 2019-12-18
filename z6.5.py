def ispisMatrice(matrica):
    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            print("%3s" % matrica[i][j], end=" ")
        print()


n = int(input())
matrica = []

for i in range(n):
    matrica.append([])
    for j in range(n):
        matrica[i].append(0)

pocetniRedIndex = 0
pocetnaKolonaIndex = 0
krajnjiRedIndex = krajnjaKolonaIndex = n

brojac = 1
while pocetniRedIndex < krajnjiRedIndex and pocetnaKolonaIndex < krajnjaKolonaIndex:
    for i in range(pocetnaKolonaIndex, krajnjaKolonaIndex):
        matrica[pocetniRedIndex][i] = brojac
        brojac += 1

    pocetniRedIndex += 1

    for i in range(pocetniRedIndex, krajnjiRedIndex):
        matrica[i][krajnjaKolonaIndex - 1] = brojac
        brojac += 1

    krajnjaKolonaIndex -= 1

    for i in range(krajnjaKolonaIndex - 1, pocetnaKolonaIndex - 1, -1):
        matrica[krajnjiRedIndex - 1][i] = brojac
        brojac += 1

    krajnjiRedIndex -= 1

    for i in range(krajnjiRedIndex - 1, pocetniRedIndex - 1, -1):
        matrica[i][pocetnaKolonaIndex] = brojac
        brojac += 1

    pocetnaKolonaIndex += 1

ispisMatrice(matrica)
