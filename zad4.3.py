a = input("Unesi broj:")
recenica = ""

while a:
    recenica += a
    a = input("Unesi broj:")

print(int(recenica[0]) + int(recenica[-1]))