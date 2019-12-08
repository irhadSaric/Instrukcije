import random

brNenapadanja = 0
for i in range(10000):
    napadajuSe = False

    prviX = random.randint(1, 8)
    prviY = random.randint(1, 8)

    drugiX = random.randint(1, 8)
    drugiY = random.randint(1, 8)

    treciX = random.randint(1, 8)
    treciY = random.randint(1, 8)

    if prviX == drugiX or prviY == drugiY:
        napadajuSe = True
    if prviX == treciX or prviY == treciY:
        napadajuSe = True
    if drugiX == treciX or drugiY == treciY:
        napadajuSe = True

    if napadajuSe:
        brNenapadanja += 1

print(brNenapadanja / 10000)