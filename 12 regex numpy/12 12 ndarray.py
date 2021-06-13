import numpy as np
a = []
n = input()
a.append(n)
z = np.array([n])

print(np.array2string(z,separator=',', formatter={'str_kind': lambda x: x}))

