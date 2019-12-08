poljeskakavca1 = int(input())
skok1 = int(input())
poljeskakavca2 = int(input())
skok2 = int(input())
poljeskakavca3 = int(input())
skok3 = int(input())
cilj = int(input())

while poljeskakavca1 <= cilj or poljeskakavca2 <= cilj or poljeskakavca3 <= cilj:
    poljeskakavca1 += skok1
    if poljeskakavca1 >= cilj:
        break
    poljeskakavca2 += skok2
    if poljeskakavca2 >= cilj:
        break
    poljeskakavca3 += skok3
    if poljeskakavca3 >= cilj:
        break

maxPolje = max(poljeskakavca1, poljeskakavca2, poljeskakavca3)

for i in range(maxPolje+1):
    if i != poljeskakavca1:
        print("-", end="")
    elif i == poljeskakavca1:
        print("*", end="")
    if i == cilj:
        print("|", end="")
print()
for i in range(maxPolje+1):
    if i != poljeskakavca2:
        print("-", end="")
    elif i == poljeskakavca2:
        print("*", end="")
    if i == cilj:
        print("|", end="")
print()
for i in range(maxPolje+1):
    if i != poljeskakavca3:
        print("-", end="")
    elif i == poljeskakavca3:
        print("*", end="")
    if i == cilj:
        print("|", end="")