import os
import csv

budget_csv = os.path.join("../PyBank", "budget_data.csv")

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)
    
    number_list = []
    sum_amount = 0
    change_list=[]
    placeholder = 0
    maxmonth = str()
    
    for row in csvreader:
        if row[0] != "":
            number_list.append(row[0])
            sum_amount += int(row[1])
            change_list.append(int(row[1]) - int(placeholder))
            placeholder = int(row[1])
        else:
            break
        
number =(len(number_list))
change_list.pop(0)
average = sum(change_list) / float(len(change_list))
minim = min(change_list)
maxim = max(change_list)
            
print("Financial Analysis\n-------------------\n" "Total months: " + str(number) + "\nTotal: " "$"+str(sum_amount) + "\nAverage Change: " + "$"+str('%.2f' % average) + "\nGreatest Increase in Profits: " + "$"+str('%.2f' % maxim) + "\nGreatest Decrease in Profits: " + "$"+str('%.2f' % minim))

with open("results.txt", "w") as file:
    file.write("Financial Analysis\n-------------------\n" "Total months: " + str(number) + "\nTotal: " "$"+str(sum_amount) + "\nAverage Change: " + "$"+str('%.2f' % average) + "\nGreatest Increase in Profits: " + "$"+str('%.2f' % maxim) + "\nGreatest Decrease in Profits: " + "$"+str('%.2f' % minim)) 


