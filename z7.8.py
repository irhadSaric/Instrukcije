listaBrojeva = []

broj = input()
while broj:
    listaBrojeva.append(int(broj))
    broj = input()

obrnutZadnji = (listaBrojeva[-1] % 10)*10
listaBrojeva[-1] = listaBrojeva[-1]//10
obrnutZadnji += listaBrojeva[-1]
del listaBrojeva[-1]

nalaziSe = False
for element in listaBrojeva:
    if element == obrnutZadnji:
        nalaziSe = True

if nalaziSe:
    print("Nalazi se")
else:
    print("Ne")

