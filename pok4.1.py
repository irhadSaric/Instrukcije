#Korisnik unosi višecifren prirodan broj. Program ispisuje razliku proizvoda i koliˇcnika najve´ce i
#najmanje cifre broja.
#najmanja*najveca - najveca/najmanja
def najvecaCifra(n):
    najveca = n % 10

    while n != 0:
        if n % 10 > najveca:
            najveca = n % 10
        n //= 10
    return najveca

def najmanja(n):
    najmanja = n % 10

    while n != 0:
        if n % 10 < najmanja:
            najmanja = n % 10
        n //= 10
    return najmanja

n = int(input())
print(najmanja(n)*najvecaCifra(n) - najvecaCifra(n)/najmanja(n))

