import re
i = input()
pattern = '\d$'
if re.search(pattern, i):
    print('True')
else:
    print('False')