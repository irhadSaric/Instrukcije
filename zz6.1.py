def sumaCifara(n):
    kopija = n
    suma = 0

    while kopija != 0:
        suma += kopija % 10
        kopija //= 10

    kopija = n
    while suma > 10:
        suma = 0
        while kopija != 0:
            suma += kopija % 10
            kopija //= 10
        kopija = suma
    return suma

n = int(input())
print(sumaCifara(n))