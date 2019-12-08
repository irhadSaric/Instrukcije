import random

nedimPobijedio = 0
aminaPobijedila = 0

for i in range(10000):
    nedimovaKocka = random.randint(1, 6)
    amininaKocka = random.randint(1, 9)
    if nedimovaKocka > amininaKocka:
        nedimPobijedio += 1
    else:
        aminaPobijedila += 1

print(nedimPobijedio / 10000)