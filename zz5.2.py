import random

nedimPobjeda = 0

for i in range(10000):
    nedimKocka = random.randint(1, 6)
    aminaKocka = random.randint(1, 9)

    if nedimKocka > aminaKocka:
        nedimPobjeda += 1

print(nedimPobjeda / 10000)