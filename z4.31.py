n = int(input())

while True:
    zbir = 0
    while n != 0:
        zbir += (n % 10) ** 2
        n //= 10
    n = zbir
    print(n)

# MORA PREKO LISTE ----