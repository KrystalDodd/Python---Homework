
import os 
import csv

#Path
py_bank = os.path.join(".\Resources\py_bank.csv")
with open(py_bank, 'r', encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csvheader = next(csvreader)
    total_months = 0
    prev_rev = 0
    rev_change = 0
    rev_average = 0
    rev_change_counter = 0
    rev_change_total = 0
    net_total  = 0
    rev_change_list = []
    greatest_increase = []
    greatest_decrese = []
    profit_losses = []
    #loop through the data 
    for row in csvreader:
        #calculate the total months
        date = row[0]
        total_months += 1
        #Calculate Total
        profit_losses = int(row[1])
        net_total = net_total + profit_losses
    for row in csvreader:
        profit_losses = int(row[1])
        prev_rev = profit_losses 
        rev_change = profit_losses - prev_rev
        rev_change_counter += 1       
        rev_change_total += rev_change
        rev_average = rev_change_total/(rev_change_counter)
        greatest_increase = max(profit_losses)
        greatest_decrese = min(profit_losses)
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total:$ {net_total}")
    print(f"Average: {rev_average}")
    print(f"Greatest Increase: {greatest_increase}")
    print(f"Greatest Decrease: {greatest_decrese}")
    
     
  
