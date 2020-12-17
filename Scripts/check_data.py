import sys
import csv
import pandas as pd

csv_file = open('./Dataset/app_basic_information.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
i = 0
for row in csv_reader:
	print(len(row))
	print(row)
	if(i == 3):
		break
	i+=1