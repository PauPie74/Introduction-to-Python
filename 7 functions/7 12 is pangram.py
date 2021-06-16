def is_pangram(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in word.lower():
            return False
    return True