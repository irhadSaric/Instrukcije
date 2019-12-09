brojevi = input()
lista = brojevi.split(" ")
for i in range(len(lista)):
    lista[i] = int(lista[i])

lokalniMaksimumi = []
for i in range(1, len(lista)-1):
    if lista[i] > lista[i-1] and lista[i] > lista[i+1]:
        lokalniMaksimumi.append(i)

print(lokalniMaksimumi[-1] - lokalniMaksimumi[0] + 1)

