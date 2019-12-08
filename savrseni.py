a = int(input())
b = int(input())

for broj in range(a, b+1):
    suma = 0
    for djelilac in range(1, broj):
        if broj % djelilac == 0:
            suma += djelilac
    if suma == broj:
        print(broj)

