def palindrom(slowo):
    if len(slowo) < 2: return True
    if slowo[0] != slowo[-1]: return False
    return palindrom(slowo[1:-1])
