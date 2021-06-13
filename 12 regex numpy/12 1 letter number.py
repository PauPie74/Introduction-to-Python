import re
i = input()
pattern = '^[A-Za-z0-9]*$'
if re.search(pattern, i):
    print('True')
else:
    print('False')