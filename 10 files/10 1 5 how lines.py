def how_lines(file):
    f = open(file, 'r')
    count = 0
    s = f.readline()
    while s != '':
        s = f.readline()
        count = count+1
    f.close()
    return count