wo = input()
wor = input()
word = input()

if word < wor:
    if wo < word and wo < wor:
        print(wo, word, wor)
    elif wo < wor and wo > word:
        print(word, wo, wor)
    else:
        print(word, wor, wo)
elif wor < word:
    if wo < word and wo < wor:
        print(wo, wor, word)
    elif wo < word and wo > wor:
        print(wor, wo, word)
    else:
        print(wor, word, wo)
