n = int(input())

for i in range(n):
    a = int(input())
    if i % 2 == 0:
        print("-"*a, end="")
    else:
        print("*"*a, end="")
    print()