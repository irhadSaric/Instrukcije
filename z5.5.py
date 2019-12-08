import random
import math

n = float(input())
ukupno = 0

for i in range(0, 10000):
    x1 = random.uniform(0, n)
    y1 = random.uniform(0, n)
    x2 = random.uniform(0, n)
    y2 = random.uniform(0, n)
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    ukupno += d
print(ukupno/10000)