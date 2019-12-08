n = int(input())

for i in range(n):
    for j in range(n*2+1):
        if i % 2 == 0:
            print("x", end="")
        else:
            if j % 2 == 1:
                print("0", end="")
            else:
                print("x", end="")
    print()