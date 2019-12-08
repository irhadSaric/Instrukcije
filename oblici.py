a = int(input())
b = int(input())

for i in range(0, a):
    for j in range(0, a):
        print("*", end="")
    print()
print("------------")
for i in range(0, a):
    for j in range(0, b):
        print("*", end="")
    print()
print("------------")

for i in range(0, a+1):
    for j in range(0, a+1):
        if i == 0 or j == 0 or i == a or j == a:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()
for i in range(a+1):
    for j in range(0, a-i):
        print(" ", end="")
    for j in range(a-i, a+i+1):
        print("*", end="")
    print()
for i in range(a+1):
    for j in range(0, i):
        print(" ", end="")
    for j in range(i, a):
        print("*", end="")
    for j in range(a, 2*a-i+1):
        print("*", end="")
    print()