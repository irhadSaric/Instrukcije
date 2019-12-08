n = int(input())

trenutniBroj = n
suma = 0

while trenutniBroj != 0:
    suma += trenutniBroj % 10
    trenutniBroj //= 10
print("Suma:", suma)
while suma > 10:
    trenutniBroj = suma
    suma = 0
    while trenutniBroj != 0:
        suma += trenutniBroj % 10
        trenutniBroj //= 10
    print("SUMA:", suma)

print(suma)