c = int(input())
r = int(input())
co = int(input())
ro = int(input())

if c > 0 and c <= 8 and r > 0 and r <= 8 and co > 0 and co <=8 and ro > 0 and ro <= 8:
    if c % 2 == 0:
        if r % 2 == 0:
            re = "white"
        else:
            re = "black"
    elif c % 2 != 0:
        if r % 2 == 0:
            re = "black"
        else:
            re = "white"
    if co % 2 == 0:
        if ro % 2 == 0:
            res = "white"
        else:
            res = "black"
    elif co % 2 != 0:
        if ro % 2 == 0:
            res = "black"
        else:
            res = "white"
    if re == res:
        print("True")
    else:
        print("False")
else:
    print("BŁĄD")