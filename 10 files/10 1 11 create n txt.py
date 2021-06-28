n = int(input())
i = 1
while n >= i:
    x = open(str(i) + ".txt", "w")
    x.close()
    i += 1