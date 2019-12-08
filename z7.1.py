negativni = []
nule = []
pozitivni = []

for i in range(10):
    n = int(input())
    if n < 0:
        negativni.append(n)
    elif n == 0:
        nule.append(n)
    else:
        pozitivni.append(n)

for element in negativni:
    print(element, end=" ")

for element in nule:
    print(element, end=" ")

for element in pozitivni:
    print(element, end=" ")

