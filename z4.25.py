n = int(input())

brojac = 0

i = 10
while brojac != n:
    suma = 0
    zapamtiBroj = i
    while i != 0:
        zadnjaCifra = i % 10
        i //= 10
        predzadnjaCifra = i % 10
        if zadnjaCifra + predzadnjaCifra == 4:
            brojac += 1
    i = zapamtiBroj + 1

print(zapamtiBroj)

