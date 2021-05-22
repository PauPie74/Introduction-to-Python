number=int(input())
num = str(number)

if number%15==0:
    print("\"FizzBuzz\"")
elif number%3==0:
    print("\"Fizz\"")
elif number%5==0:
    print("\"Buzz\"")
else:
    print("\""+num+"\"")
