i = 1
n = 0
j = -1
p = 0

while i != 0:
    i = 0
    i = int(input())
    n += 1
    if n != 1:
        if i>j:
            p += 1
    j = i


print(p)