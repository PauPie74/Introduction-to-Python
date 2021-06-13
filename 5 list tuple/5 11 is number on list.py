liczba = list(map(int,input().split()))
szukana = int(input())
index = 0

while (index<len(liczba)):
    if liczba[index] == szukana:
        print("Liczba znajduje się w liście")
        break
    else:
        index += 1

if index == len(liczba):
    print("Liczba nie znajduje się w liście")