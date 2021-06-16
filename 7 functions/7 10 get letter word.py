#Napisz funkcję o nazwie get_letter_word(word, index), która pobiera słowo oraz liczbę całkowitą. Wynikiem funkcji jest litera znajdująca się na pozycji, której wartość jest indexem.

def get_letter_word(word, index):
    l = len(word)
    if index > 0 and l >= index:
        if index == 1:
            index = 0
        else:
            index = index - 1
        letter_word = word[index]
        return letter_word
    else:
        return None