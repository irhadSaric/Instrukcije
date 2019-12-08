x = int(input())

zapamtiBroj = x
treca = zapamtiBroj % 10
zapamtiBroj //= 10
druga = zapamtiBroj % 10
zapamtiBroj //= 10
prva = zapamtiBroj

proizvod = prva*druga*treca

if treca == 5:
    print("prvo")
elif x % 2 == 1:
    print("drugo")
elif proizvod % 7 == 0:
    print("trece")
else:
    print(424)
