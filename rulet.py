import random

# hocu da igram 10000 puta rulet
# svaki od tih 10000 puta cu birati random broj na ruletu
# koja je vjrv da cu dobiti
# najveci na ruletu broj : 36

brojiPobjede = 0
for i in range(10000):
    mojBroj = random.randint(0, 36)

    ruletovBroj = random.randint(0, 36)
    
    if mojBroj == ruletovBroj:
        brojiPobjede += 1

print(brojiPobjede / 10000)