import csv
File = open('data.csv')
Reader = csv.reader(File)
for row in Reader:
    print(*row)
File.close()