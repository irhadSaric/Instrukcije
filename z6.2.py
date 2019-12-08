def crtaj(n):
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(j, end=" ")
        for j in range(1, i):
            print(j, end=" ")
        print()

n = int(input())
crtaj(n)

