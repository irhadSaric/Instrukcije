def nalaziSe(a, b):
    brojacDrugog = 0
    kopija = b
    while kopija != 0:
        brojacDrugog += 1
        kopija //= 10

    kopija = b
    brojPoklapanja = 0

    while a != 0:
        if brojPoklapanja == brojacDrugog:
            return True
        if a % 10 == kopija % 10:
            brojPoklapanja += 1
            kopija //= 10
        else:
            kopija = b
            brojPoklapanja = 0
        a //= 10
    return False

a = int(input())
b = int(input())

if nalaziSe(a, b):
    print("Nalazi se")
else:
    print("Ne nalazi se")