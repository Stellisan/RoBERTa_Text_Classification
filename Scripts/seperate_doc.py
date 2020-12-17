import sys
import csv
import pandas as pd
import re

csv_file = open('./Dataset/final_195k_detail.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
csvwritefile = open('./Dataset/AppDescriptions_notAI.csv','w')
csvwriter = csv.writer(csvwritefile)
i = 0
print '=================================================================='
for row in csv_reader:
	if(i == 2000):
		continue

	if(row[29] == ''):
		continue
		
	txt = row[29].lower()
	x = re.search("machine learning", txt)
	y = re.search("artificial intelligence", txt)
	v = re.search(" ai ", txt)
	if (not x) and (not y) and (not v):
		print '=================================================================='
		print row[29]
		csvwriter.writerow([i,row[0],row[29],0])
		print '=================================================================='
		i+=1


csvwritefile = open('./Dataset/AppDescriptions_AI.csv','w')
csvwriter = csv.writer(csvwritefile)
i = 0
print '=================================================================='
for row in csv_reader:
	#print(len(row))
	#print(row)
	#print(row[29])
	if(i == 2000):
		continue
	#csvwriter.writerow([i,row[0],row[29]])

	if(row[29] == ''):
		continue
		
	txt = row[29].lower()
	x = re.search("machine learning", txt)
	y = re.search("artificial intelligence", txt)
	v = re.search(" ai ", txt)
	if (x) or (y) or (v):
		print '=================================================================='
		print row[29]
		csvwriter.writerow([i,row[0],row[29],1])
		print '=================================================================='
		i+=1
