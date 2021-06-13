#Napisz program, który pobierze ciąg tekstowy od użytkownika, a następnie wypisze wyłącznie cyfry z tego ciągu.

import re
i = input()
s = '\d+'
r = re.findall(s, i)
print(*r,sep='\n')