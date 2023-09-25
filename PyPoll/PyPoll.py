# mport OS, CVS and
import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

#List to store Data

Ballot_ID = []
County = []
Candidate= []
Vote_Count= 0
Canidate_Count=0
Percentage = []

with open(csvpath, newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    
    for row in csvreader:  
        Ballot_ID.append(row[0])
        Vote_Count +=1
        

        
        
        
print(f'Total Votes: {Vote_Count}')


        
    