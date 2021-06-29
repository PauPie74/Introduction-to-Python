try:
    a, b = input().split()
    a = int(a)
    b = int(b)

    file = open("polish.txt",'r')

    for i in range(b):
        if i < a-1:
            line = file.readline()
        else:
            line = file.readline()
            print(line,end="")

    file.close()

except:
    print("BŁĄD")