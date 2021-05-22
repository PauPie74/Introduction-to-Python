number = float(input())
integer = int(number)
operation = number-integer
operat = format(operation,'.2')
oper = str(operat)

if oper.endswith('.0'):
    print(int(operation))
else:
    print(operat)