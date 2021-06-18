x = input()
n = 0
l = 0
d = 0
s = 0

for y in range(len(x)):
    if x[n].isdecimal():
        d += 1
    if x[n].isalpha():
        l += 1
    if x[n].isspace():
        s += 1
    n += 1

print("Ilość liter == ",l)
print("Ilość cyfr == ",d)
print("Ilość znaków białych == ",s)