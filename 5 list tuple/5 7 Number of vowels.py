string=input()
v = 0
c = 0
vowels = ["a","i"]

for ch in string:
    if (ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u' or ch=='y' or ch=='Y' or ch=='ą' or ch=='Ą' or ch=='ę' or ch=='Ę' or ch=='Ó' or ch=='ó'):
        v += 1
    else:
        c += 1

print("Liczba samogłosek:",v)
print("Liczba spółgłosek:",c)



