def funkcija():
    n = input("Unesi br: ")  # n string

    nalaziSe = False
    while n:
        if int(n) == 2:
            nalaziSe = True
        n = input("Unesi broj: ")

    return nalaziSe

if funkcija():
    print("Nalazi se")
else:
    print("Ne nalazi se")