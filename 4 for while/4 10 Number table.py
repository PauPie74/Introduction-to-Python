#Napisz program, który pobierze od użytkownika liczbę całkowitą większą od zera nn, a następnie wypisze tabelę o nn wierszach i nn kolumnach, w której to każdym ii-tym wierszu będzie występowała wartość ii.

liczba = int(input())
x = 0

for i in range(1,liczba+1):
    for j in range(liczba):
        x += 1
        if x == liczba:
            x = 0
            print (i, end='')
        else:
            print (i, end=' ')
    print()