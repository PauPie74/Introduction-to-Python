import csv
File = open('data.csv')
Reader = csv.reader(File, delimiter = '\t', lineterminator='\n')
for row in Reader:
    print(*row)
File.close()