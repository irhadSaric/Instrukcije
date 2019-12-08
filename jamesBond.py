import math
# ima n kuca (x, y)
# trenutno se nalazi u (xi, yi)
# naci najudaljeniju

n = int(input())
x0 = int(input("xi kuce"))
y0 = int(input("yi kuce"))

drugaX = int(input("x kuce"))
drugaY = int(input("y kuce"))

najudaljenija = math.sqrt((drugaX-x0)**2 + (drugaY-y0)**2)
najudaljenijax = drugaX
najudaljenijay = drugaY

for i in range(1, n-1):
    drugaX = int(input("x kuce"))
    drugaY = int(input("y kuce"))
    if math.sqrt((drugaX-x0)**2 + (drugaY-y0)**2) > najudaljenija:
        najudaljenija = math.sqrt((drugaX-x0)**2 + (drugaY-y0)**2)
        najudaljenijax = drugaX
        najudaljenijay = drugaY

k = int(input("Unesi minimalnu udaljenost"))
if najudaljenija < k:
    print("Sigurna ne postoji")
else:
    print(najudaljenija, najudaljenijax, najudaljenijay)

#hadilino@hotmail.co.uk