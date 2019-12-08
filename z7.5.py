listaGradova = []
listaB = []
listaS = []

ime = input()
while ime:
    listaGradova.append(ime)
    if ime[0] == 'b' or ime[0] == 'B':
        listaB.append(ime)
    elif ime[0] == 's' or ime[0] == 'S':
        listaS.append(ime)
    ime = input()

brojacB = 0
brojacS = 0

for ime in listaGradova:
    if ime[0] == 'b' or ime[0] == 'B':
        brojacB += 1
    elif ime[0] == 's' or ime[0] == 'S':
        brojacS += 1

if brojacB > brojacS:
    for element in listaB:
        print(element, end=" ")
elif brojacB < brojacS:
    for element in listaS:
        print(element, end=" ")
else:
    for element in listaGradova:
        if element[0] == 'b' or element[0] == 's':
            print(element, end=" ")