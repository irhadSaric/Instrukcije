import random

brojacPoteza = 0

for i in range(10000):
    brojacTriPuta = 0

    while brojacTriPuta < 3:
        kocka1 = random.randint(1, 6)
        kocka2 = random.randint(1, 6)

        if kocka1+kocka2 > 6:
            brojacTriPuta += 1
        else:
            brojacTriPuta = 0

        brojacPoteza += 1

print(brojacPoteza / 10000)
