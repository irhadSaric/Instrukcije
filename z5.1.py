import random

n = int(input("Unesi broj dobijanja n uzastopnih sestica"))

brojDobijanjaNsestica = 0

for i in range(10000):
    brojacSestica = 0
    for j in range(30):
        kockica = random.randint(1, 6)
        if kockica == 6:
            brojacSestica += 1
        else:
            brojacSestica = 0
        if brojacSestica >= n:
            brojDobijanjaNsestica += 1

print(brojDobijanjaNsestica / 10000)