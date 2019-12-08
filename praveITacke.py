x0 = float(input())
y0 = float(input())

x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

formula = (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0)

if formula > 0:
    print("P2 je sa lijeve strane prave")
elif formula < 0:
    print("P2 je sa desne strane prave")
else:
    print("P2 je na samoj pravoj")
    #Posto se tacka nalazi na pravoj mora se ispitati da li se poklapa sa nekom tackom
    #Tacka P2 se poklapa sa tačkom P1 ako su im i x i y koordinate jednake
    if x2 == x1 and y2 == y1:
        print("Poklapa se sa tačkom P1")
    elif x2 == x0 and y2 == y0:
        print("Poklapa se sa tačkom P0")
    else:
        print("Ne poklapa se ni sa jednom tačkom")
