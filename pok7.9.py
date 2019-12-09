brojevi = input()

lista = brojevi.split(" ")
for i in range(len(lista)):
    lista[i] = int(lista[i])

brojacVecih = 0
for i in range(1, len(lista)):
    if lista[i] > lista[i-1]:
        brojacVecih += 1

brojacVecihOdSume = 0
for i in range(0, len(lista)-1):
    suma = 0
    for j in range(i+1, len(lista)):
        if lista[j] > 0:
            suma += lista[j]
    if suma < lista[i]:
        brojacVecihOdSume += 1

print(brojacVecih)
print(brojacVecihOdSume)