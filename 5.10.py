import random

string = input()
minSkok = int(input())
maxSkok = int(input())

pozSkakavca2 = 0
for i in string:
    pozSkakavca2 += 1
    if i == "*":
        pozSkakavca = pozSkakavca2

pocOpasneZone = 0
krajOpasneZone = 0
brojac = 0
iteracije = 0
for i in string:
    if i == "!" and brojac == 0:
        pocOpasneZone = iteracije
        brojac += 1
    if i == "!" and brojac == 1:
        krajOpasneZone = iteracije
    iteracije += 1

pobjeda = 0
for i in range(10000):
    trenutnaPobjeda = True
    pozicijaSkakavca = pozSkakavca
    while pozicijaSkakavca < krajOpasneZone:
        pozicijaSkakavca += random.randint(minSkok, maxSkok)
        if pocOpasneZone < pozicijaSkakavca < krajOpasneZone:
            trenutnaPobjeda = False
    if trenutnaPobjeda:
        pobjeda += 1

print(pobjeda / 10000)