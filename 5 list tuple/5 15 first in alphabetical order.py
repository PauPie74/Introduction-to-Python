#Napisz program, który pobiera od użytkownika liczbę wierszy, następnie pobiera od użytkownika wiersze (którymi są ciągi znakowe), a następnie wyświetla elementy największy (w porządku leksykograficznym) dla każdego wiersza.

#Zakładamy, że ciągi znakowe są tej samej długości.

row = int(input())
i = 0
n = 0

while n < row:
    c = list(map(str, input().split()))
    min = c[i]
    max = c[i]
    while i < len(c):
        if min > c[i]:
            min = c[i]
            i += 1
        elif max < c[i]:
            max = c[i]
            i += 1
        else:
            i += 1
    print(max)
    n += 1
    i = 0