lista = []

m = int(input())
for i in range(m):
    broj = int(input())
    lista.append(broj)

lista = sorted(lista)
listaNajmanjih = lista[:m//2]
listaNajvecih = lista[m//2:]

sumaNajmanjih = 0
for element in listaNajmanjih:
    sumaNajmanjih += element

sumaNajvecih = 0
for element in listaNajvecih:
    sumaNajvecih += element

print(sumaNajvecih-sumaNajmanjih)