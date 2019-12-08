a = int(input())
brojLista = []
while a != 0:
    brojLista.append(a%10)
    a //= 10

brojLista.reverse()

nalazeSe = []
for i in range(10):
    nalazeSe.append(False)

for cifra in brojLista:
    nalazeSe[cifra] = True

while False in nalazeSe:
    suma = 0
    tempLista = []
    for cifra in brojLista:
        suma += cifra
    while suma != 0:
        tempLista.append(suma % 10)
        suma //= 10
    tempLista.reverse()
    brojLista += tempLista
    for cifra in brojLista:
        nalazeSe[cifra] = True

print(brojLista)

brojString = ""
for cifra in brojLista:
    brojString += str(cifra)

brojString = int(brojString)

suma = 0
for i in range(1, len(brojLista)+1):
    suma += brojLista[-i]*pow(10, i-1)
print("SUIMA",suma)

print(brojString)
