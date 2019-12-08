n = input()

najDuzina = 0
trenutnaDuzina = 0

for i in n:
    if int(i) > 4:
        trenutnaDuzina += 1
        if trenutnaDuzina > najDuzina:
            najDuzina = trenutnaDuzina
    else:
        trenutnaDuzina = 0

print(najDuzina)