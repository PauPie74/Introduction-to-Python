def write_to_file():
    file = open('result.txt', 'w')
    while True:
        try:
            i = input()
            file.write(i + '\n')
        except EOFError:
            file.close()
            break


write_to_file()