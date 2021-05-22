#Korzystając z tabeli ASCII (patrz poniżej) napisz program, który pobierze od użytkownika dwie liczby a,ba,b oraz wypisze znaki z tabeli ASCII z przedziału a,ba,b. Znaki te mają być oddzielone spacją. Na końcu linii ma być wyłącznie znak nowej linii.

a = int(input())
b = int(input())

for chara in range(a,b+1):
    c = chr(chara)
    print(c,"",end="")