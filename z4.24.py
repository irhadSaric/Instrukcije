m = int(input())
n = int(input())

for i in range(1, m+1):
    brojac = 1
    for j in range(1, n+1):
        print(brojac, end=" ")
        if brojac + 1 <= i:
            brojac += 1
        else:
            brojac = 1
    print()

