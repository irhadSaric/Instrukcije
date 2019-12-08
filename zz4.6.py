a = input()

i = 1
brojSead = 0
brojHarun = 0
while a:
    if i % 2 == 0:
        brojSead += float(a)
    else:
        brojHarun += float(a)
    i += 1
    a = input()

print(brojHarun - brojSead)