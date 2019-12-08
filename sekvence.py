maxBrojElemenata = 0
for i in range(1, 10000):
    trenutniBroj = i
    brojacElemenata = 0
    while trenutniBroj != 1:
        if trenutniBroj % 2 == 0:
            trenutniBroj //= 2
        else:
            trenutniBroj = 3*trenutniBroj + 1
        brojacElemenata += 1
    if brojacElemenata > maxBrojElemenata:
        maxBrojElemenata = brojacElemenata

#print(maxBrojElemenata)