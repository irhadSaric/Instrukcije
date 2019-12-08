a = int(input())
b = int(input())

prebrojCifrePrvog = 0
prebrojCifreDrugog = 0
zapamtiPrvi = a
zapamtiDrugi = b

while zapamtiPrvi != 0:
    prebrojCifrePrvog += 1
    zapamtiPrvi //= 10

while zapamtiDrugi != 0:
    prebrojCifreDrugog += 1
    zapamtiDrugi //= 10

nalaziSe = False

brojac = 0
zapamtiPrvi = a
zapamtiDrugi = b
brojIteracija = 0
pozicijaOdzada = 0

while a != 0:
    brojIteracija += 1
    if a % 10 == b % 10:
        brojac += 1
        a //= 10
        b //= 10
    else:
        a //= 10
        b = zapamtiDrugi

    if brojac == prebrojCifreDrugog:
        print(prebrojCifrePrvog - brojIteracija)
        break

if brojac != prebrojCifreDrugog:
    print(-1)