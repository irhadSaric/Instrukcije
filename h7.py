a = input()
suma = 0

while a != "-1":
    suma += int(a) % 10
    a = input()

print(suma)