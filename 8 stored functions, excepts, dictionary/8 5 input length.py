#Napisz program, który będzie pobierał od użytkownika ciąg tekstowy (do momentu napotkania linii wyłącznie ze znakiem spacji), a następnie wypisze ilość wprowadzonych przez użytkownika słów.

x = "x"
l = 0

while x != " ":
    x = input()
    l += len(x.split())

print(l)