lista = []

n = input()
while n:
    lista.append(int(n))
    n = input()

najamnji = lista[0]
for i in range(0, len(lista)//2):
    if lista[i] < najamnji:
        najamnji = lista[i]

najveci = lista[len(lista)//2]
for i in range(len(lista)//2, len(lista)):
    if lista[i] > najveci:
        najveci = lista[i]

for i in range(najamnji, najveci, 2):
    print(i, end=" ")

