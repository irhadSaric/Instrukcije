fajl = open('haretest01.in', 'r')

matrica = []

red = fajl.readline()
while red != '':
    podaci = red.split()
    matrica.append(podaci)
    red = fajl.readline()

print(matrica)

najkraca = len(matrica[0][0])
for red in matrica:
    for kolona in red:
        if len(kolona) < najkraca:
            najkraca = len(kolona)

print(najkraca)

if len(matrica) > najkraca or len(matrica[0]) > najkraca:
    print("Da")
else:
    print("Ne")