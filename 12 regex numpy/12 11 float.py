import re
i = input()
pattern = '^\d*[.][0-9]{0,2}'
if re.search(pattern, i):
    print('True')
else:
    print('False')