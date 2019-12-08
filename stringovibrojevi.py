n = int(input())

proizvod = 1
while n != 0:
    zadnja = n % 10
    if zadnja % 2 != 0 and zadnja < 6:
        proizvod *= zadnja
    n //= 10

print(proizvod)

n = input()
proizvod = 1
for cifra in n:
    if int(cifra) % 2 != 0 and int(cifra) < 6:
        proizvod *= int(cifra)
print(proizvod)