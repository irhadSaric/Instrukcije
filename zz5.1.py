import random

n = int(input("Unesi br ponavljanja"))

pobjeda = 0
for simulacija in range(10000):
    brojac = 0
    for j in range(30):
        kockica = random.randint(1, 6)
        if kockica == 6:
            brojac += 1
        else:
            brojac = 0
        if brojac >= n:
            pobjeda += 1

print(pobjeda / 10000)
