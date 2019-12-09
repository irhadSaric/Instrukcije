lista = []

rijec = input()
while rijec:
    lista.append(rijec)
    rijec = input()

prosjek = 0
for element in lista:
    prosjek += len(element)

prosjek //= len(lista)

for element in lista:
    if len(element) > prosjek:
        print(element, end=" ")