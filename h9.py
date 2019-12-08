a = input()

suma = 0
"""
while a != "-1":
    if int(a) >= 10:
        suma += (int(a) // 10) % 10
    else:
        suma += int(a)
    a = input()
"""

while a != "-1":
    if int(a) >= 10:
        suma += int(a[-2])
    else:
        suma += int(a[-1])
    a = input()
print(suma)
