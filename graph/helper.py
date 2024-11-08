import random
import csv

header = ['column1', 'column2']

with open ('randomData.csv','w',encoding='UTF8',newline='') as outputFile:
	writer = csv.writer(outputFile)
	writer.writerow(header)
	for i in range (100):
		currentRow = []
		random_value = random.randint(1,34)
		currentRow.append(i)
		currentRow.append(random_value)
		writer.writerow(currentRow)

