import random

stanje = int(input())
ulog = int(input())
zeljenoStanje = int(input())

dobitak = 0
for i in range(100):
    trenutnoStanje = stanje
    while trenutnoStanje > 0 and trenutnoStanje < zeljenoStanje:
        broj = random.randint(1, 100)
        if broj <= 49:
            trenutnoStanje += ulog
        else:
            trenutnoStanje -= ulog
        print(trenutnoStanje, i)
    if trenutnoStanje >= zeljenoStanje:
        dobitak += 1

print(dobitak / 10000)