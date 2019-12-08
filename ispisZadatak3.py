"""
12345
51234
45123
34512
23451
"""

n = int(input())

for i in range(n, 0, -1):
    for j in range(n, i, -1):
        print(j, end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()