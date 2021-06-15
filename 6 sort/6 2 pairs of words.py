#Napisz program, który pobierze ciąg napisów (zapisanych w jednej linii oddzielonych spacją) oraz wypisze pary słów, które nie są w odpowiedniej kolejności (w porządku rosnącym) tzn. w parze o indeksach i,j jeżeli i-te słowo jest większe niż j-te słowo to wypisuje parę tych słów (patrz przykłady poniżej).

words = str(input())
#012, 456, 8910
i = 0

lw = len(words.split())
ll = len(words.split()[0])

while lw-1 > 0:
    lw -= 1
    first_word = words.split()[i]
    second_word = words.split()[i+1]
    if first_word > second_word:
        print(first_word,second_word)
    i += 1