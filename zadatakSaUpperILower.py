brojStepeni = float(input())
jedinica = input()

jedinica = jedinica.lower()

if jedinica == "cls":
    rezultat = (9 / 5) * brojStepeni + 32
    print(str(rezultat) + "Fhr")
elif jedinica == "fhr":
    rezultat = (5 / 9) * (brojStepeni - 32)
    print(str(rezultat) + "Cls")
else:
    print("Pogresna jedinica")

"""
Unesi broj stepeni i mjernu jedinicu.
Pošto se jedinica moze unijeti i kao FHR, Fhr,FhR ili CLS, Cls, cls ili bilo koja kombinacija velikih i malih slova
    potrebno je jedinicu pretvoriti u samo mala slova ili samo velika slova radi lakšeg ispitivanja
    Da nije vrseno pretvarane jedinice u samo mala slova bilo bi više uslova npr.
    if jedinica == "CLS" or jedinica == "CLs" or jedinica == "Cls" or jedinica == "cls" or jedinica == "cLS"
        or jedinica == "cLs" or jedinica == "clS":
        #radi pretvaranje u farenhajte
    Posto je urađena konverzija jedinice u samo mala slova dovoljno je da se uradi samo
    if jedinica == "cls":
        #radi pretvaranje

"""
