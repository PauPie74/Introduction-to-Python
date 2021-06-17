try:
    a = int(input())
    b = int(input())
    print(a/b)
except ValueError:
    print("Błędny format danych liczbowych!")
except ZeroDivisionError:
    print("Nie dziel przez zero!")