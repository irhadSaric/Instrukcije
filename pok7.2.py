n = int(input())
lista = []

for i in range(n):
    broj = int(input())
    lista.append(broj)

print(lista)

m = int(input())

#print(lista[-1])
#print(lista[:m])
#print(lista[m:])
print(lista[m:-m])