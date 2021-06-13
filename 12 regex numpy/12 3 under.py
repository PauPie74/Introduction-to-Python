#Napisz program, który pobierze ciąg tekstowy od użytkownika, a następnie wypisze wartość True, jeżeli ciąg ten składa się na początku z conajmniej jednej małej litery, potem znaku podkreślenie oraz zakończy się conajmniej jedną małą literą w dowolnym miejscu tego ciągu lub False w przeciwnym przypadku.

import re
i = input()
pattern = '^[a-z]*_[a-z]*$'
if re.search(pattern, i):
    print('True')
else:
    print('False')