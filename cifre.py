a = int(input("Unesi broj"))
suma = 0

while a != 0:
    zadnjaCifra = a % 10
    if zadnjaCifra % 2 == 0:
        suma += zadnjaCifra
    a = a // 10

print(suma)
