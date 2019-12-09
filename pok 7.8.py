lista = []

broj = input()
while broj:
    lista.append(broj)
    broj = input()

obrnutZadnji = lista[-1][1] + lista[-1][0]

nalaziSe = False
for element in lista:
    if element == obrnutZadnji:
        nalaziSe = True

if nalaziSe:
    print("Da")
else:
    print("Ne")


"""a = "23"

obrnutBroj = a[1] + a[0]
print(obrnutBroj)"""
