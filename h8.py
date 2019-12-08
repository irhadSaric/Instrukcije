n = int(input()) #broj redova

for i in range(n):
    brojZvjezdicaIliCrtica = int(input())

    if i % 2 == 0:
        for j in range(brojZvjezdicaIliCrtica):
            print("-", end="")
    else:
        for j in range(brojZvjezdicaIliCrtica):
            print("*", end="")
    print()