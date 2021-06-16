def get_largest_size(words):
    l = len(words)
    i = 0
    while i != l-1:
        if len(words[i]) > len(words[i+1]):
            m = words[i]
        else:
            m = words[i+1]
        i += 1
    if l == 1:
        m = words[0]
    largest_size = len(m)
    return largest_size
