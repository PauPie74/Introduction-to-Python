list = 5 * [0]
index = 0
while (index < len(list)):
    list[index] = int(input())
    index += 1

tuple = tuple(list)
print(tuple)