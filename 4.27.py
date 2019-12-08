n = int(input())

najduziRaspon = 0
najduziBroj = ""

trenutnaDuzina = 0
trenutniBroj = ""
for i in str(n):
    if int(i) > 4:
        trenutnaDuzina += 1
        trenutniBroj += i
        if trenutnaDuzina > najduziRaspon:
            najduziBroj = trenutniBroj
    else:
        trenutnaDuzina = 0
        trenutniBroj = ""

print(najduziBroj)