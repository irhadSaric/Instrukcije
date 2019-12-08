# Korisnik unosi paran broj brojeva
# stavlja ih u listu
# Traži minimalan broj u prvoj polovini liste
# Trazi max broj u drugoj polovini liste
# ispisuje svaki drugi broj između gornja 2

lista = []
broj = input()
while broj:
    lista.append(int(broj))
    broj = input()

najmanji = min(lista[:len(lista)//2])
najveci = max(lista[len(lista)//2:])

for i in range(najmanji, najveci+1, 2):
    print(i)


"""lista = [1, 2, 3, 4, 5, 6, 7]
print(lista[2:4])
print(lista[:len(lista)//3])
print(lista[len(lista)//2:])"""