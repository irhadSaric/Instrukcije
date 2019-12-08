import random

brojSudara = 0
for i in range(10000):
    x1 = 0
    y1 = 0
    x2 = 2
    y2 = 0
    brojKoraka1 = 0
    brojKoraka2 = 0
    sudar = False
    while brojKoraka1 <= 10 and brojKoraka2 <= 10 and not sudar:
        smjer1 = random.randint(1, 4)
        smjer2 = random.randint(1, 4)
        if smjer1 == 1:
            x1 += 1
        elif smjer1 == 2:
            x1 -= 1
        elif smjer1 == 3:
            y1 += 1
        else:
            y1 -= 1

        brojKoraka1 += 1

        if x1 == x2 and y1 == y2:
            brojSudara += 1
            sudar = True
        else:
            if smjer2 == 1:
                x2 += 1
            elif smjer2 == 2:
                x2 -= 1
            elif smjer2 == 3:
                y2 += 1
            else:
                y2 -= 1

            brojKoraka2 += 1

            if x1 == x2 and y1 == y2:
                brojSudara += 1
                sudar = True

print(brojSudara / 10000)