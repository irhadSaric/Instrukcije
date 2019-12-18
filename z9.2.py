fajl = open('test02.in', 'r')

red = fajl.readline()
while red != '':
    podaci = red.split();
    if podaci[0] == podaci[1] or len(podaci[1]) < 5 or "1234" in podaci[1]:
        print(podaci[0], podaci[1])
    red = fajl.readline()
