n = int(input())
lista = []

for i in range(n):
    broj = int(input())
    lista.append(broj)

m = int(input())
for i in range(m):
    lista.remove(min(lista))
    lista.remove(max(lista))

print(lista)