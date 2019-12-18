fajl = open('test01.in', 'r')

suma = 0
linija = fajl.readline()
while linija != '':
    brojevi = linija.split()
    for i in range(len(brojevi)):
        suma += float(brojevi[i])
    linija = fajl.readline()

print(suma)