n = int(input())
sum = 0

while (n < 0):
    n = n * -1

while (n > 0):
    dig = n % 10
    sum += dig
    n = n // 10

print(sum)
