for i in range(10, 100):
    zapamtiBroj = i
    abc = i ** 2
    if abc % 10 == i % 10:
        abc //= 10
        i //= 10
        if abc % 10 == i % 10:
            print(zapamtiBroj)

