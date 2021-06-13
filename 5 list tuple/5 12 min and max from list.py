n = list(map(int, input().split()))
i = 0
min = n[i]
max = n[i + 1]

while i < len(n):
    if min > n[i]:
        min = n[i]
    if max < n[i]:
        max = n[i]
    i += 1

print("min ==", min)
print("max ==", max)