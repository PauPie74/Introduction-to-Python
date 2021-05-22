liczba = int(input())

litera = input()
l = ord(litera)-96 #a = 97
lit = ord(litera)
literka = 97

for i in range(1,liczba+1):
    for j in range(l):
        if literka+j == lit:
            print (str(i)+chr(literka+j))
        else:
            print (str(i)+chr(literka+j), end=',')
print()

