def upper_first_column():
    file = open('test.txt', 'r')
    text = []

    for line in file:
        line_list = line.split()
        line_list[0] = line_list[0].upper()
        line_modified = ' '.join(line_list)
        text.append(line_modified)

    file.close()

    file_to_write = open('test_result.txt', 'w')
    for line_to_write in text:
        file_to_write.write(line_to_write + '\n')

    file_to_write.close()


upper_first_column()