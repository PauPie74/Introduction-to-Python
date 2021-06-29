import csv
outputFile = open('data.csv','w',newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow([10,'a1', 1])
outputWriter.writerow([12,'a2', 3])
outputWriter.writerow([14, 'a3', 5])
outputWriter.writerow([16, 'a4', 7])
outputWriter.writerow([18, 'a5', 9])
outputFile.close()