string=input()
a = 0
b = -1
w = "X"

while a < len(string):
    if string[a] == string[b]:
        w = "True"
    else:
        w = "False"
        break
    a += 1
    b -= 1

print(w)