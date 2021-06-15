a = input().split()
i = len(a)

while i != 0:
    j = 0
    while j < i - 1:
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        j += 1
    i -= 1

print(*a)