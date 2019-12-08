predzadnji = int(input())
zadnji = int(input())

drugi = zadnji
n = input()
while n:
    temp = zadnji
    zadnji = int(n)
    predzadnji = temp
    n = input()

print(predzadnji, drugi)