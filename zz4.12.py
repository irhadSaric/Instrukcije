n = int(input())

sumaHarun = 0
sumaSead = 0

brojUzetih = 0
for i in range(1, n):
    if i % 2 != 0:
        for j in range(i):
            if brojUzetih < n:
                a = int(input())
                brojUzetih += 1
                sumaSead += a
    else:
        for j in range(i):
            if brojUzetih < n:
                a = int(input())
                brojUzetih += 1
                sumaHarun += a

print(sumaHarun, sumaSead)