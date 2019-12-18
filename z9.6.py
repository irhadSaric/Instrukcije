fajl = open('test06.in', 'r')

matrica = []

red = fajl.readline()
while red != '':
    podaci = red.split()
    matrica.append(podaci)
    red = fajl.readline()

redoviSavrseni = True

for i in range(len(matrica)):
    originalRijec = ""
    for j in range(len(matrica[i])):
        originalRijec += matrica[i][j]
    matrica[i].reverse()

    obrnutaRijec = ""
    for j in range(len(matrica[i])):
        obrnutaRijec += matrica[i][j]
    matrica[i].reverse()

    if originalRijec != obrnutaRijec:
        redoviSavrseni = False

koloneSavrsene = True
for i in range(len(matrica)):
    originalRijec = ""
    for j in range(len(matrica[i])):
        originalRijec += matrica[j][i]

    obrnutaRijec = ""
    for slovo in originalRijec:
        obrnutaRijec = slovo + obrnutaRijec

    if originalRijec != obrnutaRijec:
        koloneSavrsene = False

print(koloneSavrsene, redoviSavrseni)
if koloneSavrsene and redoviSavrseni:
    print("Savrsena")
elif koloneSavrsene or redoviSavrseni:
    print("Polusavrsena")
else:
    print("Nesavrsena")
    #print(matrica[i], matrica[i][::-1])