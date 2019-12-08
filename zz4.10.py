n = int(input())

brojacProgr = 0

for i in range(n):
    rijec = input()
    if rijec == "programiranje":
        brojacProgr += 1

if brojacProgr == 2:
    print("jeste")
else:
    print("nije")
