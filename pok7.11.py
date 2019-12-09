n = int(input())

matrica = []
for i in range(n):
    red = []
    for j in range(n):
        broj = int(input())
        red.append(broj)
    matrica.append(red)

for j in range(n):
    sumaKolone = 0
    for i in range(n):
        sumaKolone += matrica[i][j]
    print(sumaKolone)