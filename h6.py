sumaHarunovih = 0
sumaSeadovih = 0

a = input()
i = 1
while a:
    if i % 2 == 0:
        sumaSeadovih += float(a)
    else:
        sumaHarunovih += float(a)
    i += 1
    a = input()

print(sumaHarunovih - sumaSeadovih)