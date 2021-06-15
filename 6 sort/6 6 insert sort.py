a = input().split()
n = len(a)
i = 0

for i in range(1, n):
    k = a[i]
    j = i - 1
    while j >= 0 and k > a[j]:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = k

print(*a)

