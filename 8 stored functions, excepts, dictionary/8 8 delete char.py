w = str(input())

try:
    i = int(input())
except ValueError:
    i = int(input())

w = w.replace(w[i], '',1)
print(''.join(w))