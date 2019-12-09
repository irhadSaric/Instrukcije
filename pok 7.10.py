#matrica = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#matrica = []

n = int(input())

matrica = []
for i in range(n):
    red = []
    for j in range(n):
        broj = int(input())
        red.append(broj)
    matrica.append(red)

sumaGlavne = 0
for i in range(n):
    for j in range(n):
        if i == j:
            sumaGlavne += matrica[i][j]

sumaSporedne = 0
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            sumaSporedne += matrica[i][j]

print(matrica)
print(sumaGlavne)
print(sumaSporedne)
print(sumaGlavne*sumaSporedne)