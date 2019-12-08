def nalaziSe(broj1, broj2):
    brojacPogotaka = 0

    brojacCifara = 0
    kopija2 = broj2
    while kopija2 != 0:
        kopija2 //= 10
        brojacCifara += 1

    kopija2 = broj2
    while broj1 != 0:
        if broj1 % 10 == kopija2 % 10:
            brojacPogotaka += 1
            kopija2 //= 10
        else:
            brojacPogotaka = 0
            kopija2 = broj2
        broj1 //= 10
        if brojacCifara == brojacPogotaka:
            return True
    return False


if nalaziSe(1234567868, 246):
    print("Nalazi se")
else:
    print("Ne nalazi se")