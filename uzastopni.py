n = int(input())

postojeUzastopni = False

prvi = int(input())
for i in range(n-1):
    drugi = int(input())
    if abs(prvi - drugi) == 1:
        postojeUzastopni = True
    prvi = drugi

if postojeUzastopni:
    print("Postoje uzastopni")
else:
    print("Ne")