#Napisz program, który będzie liczył iloczyn liczb całkowitych wprowadzanych przez użytkownika liczb do momentu wprowadzenia przez użytkownika wartości 0. Program ma wypisać obliczona wartość. W przypadku podania od razu liczby 0 program ma wypisać wartość 1.

iloczyn = int(input())

if iloczyn == 0:
    print("1")
else:
    while (True):
        n = int(input())
        if n == 0:
            break
        else:
            iloczyn *= n
    print(iloczyn)
