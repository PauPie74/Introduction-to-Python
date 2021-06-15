a = input().split()
n = len(a)
i = 0

for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if a[min_idx] > a[j]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]

print(*a)