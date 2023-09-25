#import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

#Lists to store data

Date = []
PL = []
MonthCount = 0
PLSum = 0
Change = 0
total_change = []
AvgRevenue= []
increase = []
decrease = []



# WITH OPEN
with open(csvpath, newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    next(csvreader, None)


    for row in csvreader:
        Date.append(row[0])
        PL.append(row[1])
        
#Total Month Count and Sum of 
        MonthCount += 1
        PLSum += int(row[1])
        
        
AvgRevenue = PLSum / (MonthCount - 1)


#Print with Dicitonaries
print(f'Total Months: {MonthCount}')
print(f'Total Revenue: ${PLSum}')
print(f'Average: ${round(AvgRevenue,2)}')
#print(avg)
