fajl = open('hare2.in', 'r')

matrica = []

red = fajl.readline()
while red != '':
    podaci = red.split()
    temp = []
    for i in podaci:
        temp.append(int(i))
    matrica.append(temp)
    red = fajl.readline()

print("izvuceni podaci iz fajla: ", matrica)
brojRedova = matrica[0][0]
brojKolona = matrica[1][0]
print("broj redova:", brojRedova)
print("broj kolona:", brojKolona)

matricaBrojeva = []
for i in range(2, len(matrica)):
    matricaBrojeva.append(matrica[i])

print("matrica brojeva", matricaBrojeva)

sortiranaMatrica = []
for red in matricaBrojeva:
    sortiranaMatrica.append(sorted(red))

print("sortirana matrica:", sortiranaMatrica)
fina = True
for j in range(brojKolona):
    for i in range(brojRedova-1):
        if sortiranaMatrica[i+1][j] < sortiranaMatrica[i][j]:
            fina = False
if fina:
    print("Fina")
else:
    print("Nije fina")

