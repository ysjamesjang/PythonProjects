import os
import csv
import sys

poll_csv = os.path.join("../PyPoll", "election_data.csv")

with open(poll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)
    
    number_list = []
    candidates_list = []
    full_cand_list = []
    candidates_count = []

#Loop across the entire csv file and add voter ID to a list, then count the items on the list to get the count. On a second list, add Candidates.
    for row in csvreader:
        if row[0] != "":
            number_list.append(row[0])
            full_cand_list.append(row[2])
            #Add unique instance of Candidate for each non-empty row
            if row[2] not in candidates_list:
                candidates_list.append(row[2])
        else:
            break

#Create a list of counts for each individual candidate
    for x in candidates_list:
        candidates_count.append(full_cand_list.count(x))
        
        
number =(len(number_list))

#Print the results to terminal
print("Election Results\n-------------------" + "\nTotal Votes: " + str(number) +"\n-------------------")

for a in range(0,4):
    data = print(str(candidates_list[a]) + " {0:.3%}".format(int(candidates_count[a])/sum(candidates_count)) + " (" +str(candidates_count[a]) + ")")

print("-------------------" + "\nWinner: " + str(max(set(full_cand_list), key=full_cand_list.count)) + "\n-------------------")

#Create text file with results
f = open("result.txt", 'w')
sys.stdout = f

print("Election Results\n-------------------" + "\nTotal Votes: " + str(number) +"\n-------------------")

for a in range(0,4):
    data = print(str(candidates_list[a]) + " {0:.3%}".format(int(candidates_count[a])/sum(candidates_count)) + " (" +str(candidates_count[a]) + ")")

print("-------------------" + "\nWinner: " + str(max(set(full_cand_list), key=full_cand_list.count)) + "\n-------------------")

f.close()
