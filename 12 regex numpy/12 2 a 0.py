#Napisz program, który pobierze ciąg tekstowy od użytkownika, a następnie wypisze wartość True, jeżeli ciąg ten składa się wyłącznie z litery a, a następnie zero lub więcej wystąpień litery b, a na końcu dowolny znak lub False w przeciwnym przypadku.

import re
i = input()
pattern = '^[aA]b*.$'
if re.search(pattern, i):
    print('True')
else:
    print('False')




