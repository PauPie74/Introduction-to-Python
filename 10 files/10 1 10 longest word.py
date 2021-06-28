with open("polish.txt",'r') as f:
    words = f.read().split()
    maxlen = max(words,key=len)
    print(maxlen)
