import random

pocetniX = 0
pocetniY = 0
vracenNaPocetak = 0

for i in range(10000):
    for j in range(10):
        potez = random.randint(1, 4)
        if potez == 1:
            pocetniY += 1
        elif potez == 2:
            pocetniY -= 1
        elif potez == 3:
            pocetniX += 1
        else:
            pocetniX -= 1
    if pocetniX == 0 and pocetniY == 0:
        vracenNaPocetak += 1
    pocetniX = 0
    pocetniY = 0

print(vracenNaPocetak / 10000)
