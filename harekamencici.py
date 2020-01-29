unos = input()

lista = unos.split()
for i in range(len(lista)):
    lista[i] = int(lista[i])

print(lista)

while len(lista) >= 0:
    if len(lista) == 1:
        break
    lista = sorted(lista)
    print(lista)
    najveci = lista[-1]
    drugi_najveci = lista[-2]
    pom_lista = lista[0:len(lista)-2]

    if drugi_najveci != najveci:
        pom_lista.append(abs(najveci-drugi_najveci))

    lista = pom_lista

print(lista)

if len(lista) > 0:
    print(lista[0])
else:
    print(0)

#2 7 4 1 8 1