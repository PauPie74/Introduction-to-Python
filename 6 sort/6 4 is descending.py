#Napisz program, który pobierze ciąg napisów (zapisanych w jednej linii oddzielonych spacją) i sprawdzi czy dany ciąg jest posortowany rosnąco (czyli od najmniejszego słowa do największego).

words = str(input())
i = 0

l = len(words.split())

while l > 0:
    first_word = words.split()[i]
    second_word = words.split()[i+1]
    if first_word > second_word:
        print("Ciąg nie jest posortowany rosnąco")
        break
    else:
        i += 1
        if i+1 == l:
            print("Ciąg jest posortowany rosnąco")
            break

#Ciąg jest posortowany rosnąco
#Ciąg nie jest posortowany rosnąco"