import csv
File = open('data.csv')
Reader = csv.reader(File, delimiter = '\t', lineterminator='\n')
next(Reader)
for row in Reader:
    print(*row)
File.close()