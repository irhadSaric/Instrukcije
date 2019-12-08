n = input()

while n:
    if int(n) < 1000:
        print(n)
        n = input()
    else:
        brojRecenica = ""
        n = int(n)
        brojacUzetih = 0
        while n != 0:
            zadnjaCifra = n % 10
            brojRecenica = str(zadnjaCifra) + brojRecenica
            brojacUzetih += 1
            if brojacUzetih == 3:
                brojRecenica = "." + brojRecenica
                brojacUzetih = 0
            n //= 10
        print(brojRecenica)
        n = input()
