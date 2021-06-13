import re
i = input()
s = input()
r = re.findall(s, i)
print(len(r))