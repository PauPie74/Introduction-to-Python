n = list(map(int, input().split()))
i = 0
s = 0

while i < len(n):
    s += n[i]
    i += 1

print(s)