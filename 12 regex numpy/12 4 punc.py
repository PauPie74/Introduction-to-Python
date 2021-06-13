#Napisz program, który pobierze ciąg tekstowy od użytkownika, a następnie wypisze wartość True, jeżeli ciąg ten na końcu wiersza posiada słowo plus ewentualnie znak interpunkcyjny lub False w przeciwnym przypadku.

import re
i = input()
pattern = 'plus$|[.|,|;|:|-|...|?|!|(|)|"]$'
if re.search(pattern, i):
    print('True')
else:
    print('False')