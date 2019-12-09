n = int(input())
lista = []

for i in range(n):
    broj = int(input())
    lista.append(broj)

kopijaLista = sorted(lista)
medijana = kopijaLista[len(kopijaLista)//2]

lista.remove(medijana)
print(lista)
