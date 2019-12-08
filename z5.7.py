import random

brojUspjeha = 0
for i in range(10000):
    strA = random.randint(1, 100)
    strB = random.randint(1, 100)
    strC = random.randint(1, 100)
    if strA + strB > strC and strB + strC > strA and strC + strA > strB:
        brojUspjeha += 1

print(brojUspjeha / 10000)