#Napisz program, który pobierze od użytkownika imię oraz liczbę rzeczywistą określający jego zarobki.
#Następnie program ma wyswietlić imię podane przez użytkownika oraz dwukrotność jego zarobków.
#Zarobki zaokrąglamy na drugiego miejsca po przecinku.

name = input()
salary = float(input())

print(name+":",format(2*salary,'.2f'))