fajl = open('test03.in', 'r')

kurs1 = []
kurs2 = []
kurs3 = []

red = fajl.readline()
while red != '':
    podaci = red.split()
    if podaci[2] == '1':
        kurs1.append(podaci[0]+" "+podaci[1])
    elif podaci[2] == '2':
        kurs2.append(podaci[0]+" "+podaci[1])
    elif podaci[2] == '3':
        kurs3.append(podaci[0]+" "+podaci[1])
    red = fajl.readline()

print(kurs1)
print(kurs2)
print(kurs3)