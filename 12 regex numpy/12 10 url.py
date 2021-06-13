#Napisz program, który pobierze ciąg tekstowy od użytkownika, a następnie wypisze wszystkie linki z tego ciągu.

#Uwaga: Portal stepik.org ma problem z interpretacją linków. Dlatego wszystkie linki tutaj zamiast // mają ////. W rozwiązaniu w środowisku Pycharm używaj linków z //.

import re

i = input()

s = 'https:////[a-zA-z0-9]*\.com|https:////[a-zA-z0-9]*\.pl|http:////[a-zA-z0-9]*\.?com|http:////[a-zA-z0-9]*\.?pl'
d = re.findall(s,i)
print(d)

