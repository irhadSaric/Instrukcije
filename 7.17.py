brojevi = input()

listaBrojeva = brojevi.split()

for i in range(len(listaBrojeva)):
    listaBrojeva[i] = int(listaBrojeva[i])

maksimalni = 1
trenutniMax = 1
for i in range(len(listaBrojeva)):
    trenutniMax = 1
    for j in range(i, len(listaBrojeva)):
        if listaBrojeva[i] == listaBrojeva[j]:
            trenutniMax = j - i + 1
            if trenutniMax > maksimalni:
                maksimalni = trenutniMax

print(maksimalni)