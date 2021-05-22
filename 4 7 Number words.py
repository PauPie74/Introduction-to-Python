#Napisz program, który pobierze od użytkownika liczbę całkowitą większa od zera, a następnie pobierze nn słów i wyświetli je na ekran.

#W przypadku nieprawidłowych danych program ma ponownie pobrać dane od użytkownika.

n = int(input())

while (n < 1):
    n = int(input())

for word in range(1, n + 1):
    w = input()
    print(w)