a = input()
stringBrojeva = ""

while a:
    stringBrojeva += a
    a = input()

print(int(stringBrojeva[1])*int(stringBrojeva[-2]))