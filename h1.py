a = int(input("Unesi broj"))

stringBroja = str(a)
min = int(stringBroja[0])
max = int(stringBroja[0])
for cifra in stringBroja:
    if int(cifra) < min:
        min = int(cifra)
    if int(cifra) > max:
        max = int(cifra)

print(min*max - max/min)