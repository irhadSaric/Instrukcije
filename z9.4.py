fajl = open('test04.in', 'r')

matrica = []
red = fajl.readline()
while red != '':
    podaci = red.split()
    matrica.append(podaci)
    red = fajl.readline()

m1 = matrica[:len(matrica)//2]
m2 = matrica[len(matrica)//2:]

suma = 0
for i in range(len(m2)):
    for j in range(len(m2[i])):
        if m2[i][j] == '*':
            suma += int(matrica[i][j])

print(suma)