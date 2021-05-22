#Napisz program, który wypisze liczby od 1 do n, gdzie n jest podane przez użytkownika. W przypadku błędnych danych program powinien wypisać komunikat BŁĄD oraz zakończyć działanie.

n = int(input())

while (n<1):
    print("BŁĄD")
    break
for i in range(1,n+1):
    print(i)
