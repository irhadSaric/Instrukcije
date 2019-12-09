listaGradova = []

grad = input()
while grad:
    listaGradova.append(grad)
    grad = input()

brojacS = 0
brojacB = 0

for element in listaGradova:
    if element[0] == 'S':
        brojacS += 1
    if element[0] == 'B':
        brojacB += 1

if brojacS > brojacB:
    for element in listaGradova:
        if element[0] == 'S':
            print(element, end=" ")
elif brojacB > brojacS:
    for element in listaGradova:
        if element[0] == 'B':
            print(element, end=" ")
else:
    for element in listaGradova:
        print(element, end=" ")