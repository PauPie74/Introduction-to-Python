a = int(input())  # długość
b = int(input())  # szerokość

if a == 1 or b == 1:
    for i in range(1):
        print(b * "*")

else:
    for i in range(1):
        print(b * "*")

    for i in range(a - 2):
        print("*" + (b - 2) * " " + "*")

    for i in range(1):
        print(b * "*")
