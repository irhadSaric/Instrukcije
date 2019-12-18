fajl = open('test05.in', 'r')

matrica = []
red = fajl.readline()
while red != '':
    podaci = red.split()
    matrica.append(podaci)
    red = fajl.readline()

pocX = pocY = 0
for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        if matrica[i][j] == 'R':
            pocX = i
            pocY = j

koraci = 0
while pocY < len(matrica[pocX]) and matrica[pocX][pocY+1] == '-':
    pocY += 1
    koraci += 1

if pocY == len(matrica[pocX]) - 1:
    print('Da', koraci+1)
else:
    while pocX < len(matrica) and matrica[pocX+1][pocY] == '-':
        pocX += 1
        koraci += 1
    if pocX == len(matrica)-1:
        print('Da', koraci+1)
    else:
        print('Ne')