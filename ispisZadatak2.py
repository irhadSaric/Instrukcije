n = int(input())

for i in range(1, n+1):
    for j in range(i, n+1):
        print(j, end=" ")
    for j in range(1, i):
        print(j, end=" ")
    print()

"""
2. Napisati funkciju koja kao parametar prima vrijednost n, a potom iscrtava figuru:
za n = 7
i = 1: 1 2 3 4 5 6 7
i = 2: 2 3 4 5 6 7 1
i = 3: 3 4 5 6 7 1 2
i = 4: 4 5 6 7 1 2 3
i = 5: 5 6 7 1 2 3 4
i = 6: 6 7 1 2 3 4 5
i = 7: 7 1 2 3 4 5 6

Vidiš da se u svakom redu ispisuju prvo brojevi od 1 do n, a zatim se ispisuju brojevi od 1 do i
"""