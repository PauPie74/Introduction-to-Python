import numpy as np

x = input().split()

a = int(x[0])
b = int(x[1])
c = a*b

x = np.arange(c)
y = x.reshape(a,b)
print(y)