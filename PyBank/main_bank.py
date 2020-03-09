# Dependencies
import os
import csv

# READ CSV

# first get the wd
dir_path = os.path.dirname(os.path.realpath(__file__)) # store the name of the wd
budget_csvpath = os.path.join(dir_path, 'budget_data.csv') # get the file fromthe current wd

# Initialize a list to store the rows
rows = []

with open(budget_csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for ii in csvreader:
        rows.append(ii)

# NUMBER OF MONTHS

# The number of months is the number of rows because there is an entry for each month
total_months = len(rows)

# TOTAL PROFIT/LOSS

# Initialize a profit/loss sum variable
total_profit_loss = 0

# Add all the profit/loss differenes from change_list
for i in range(len(rows)):
    total_profit_loss += int(rows[i][1])

# AVERAGE CHANGE

# Initialize an empty list
change_list = []

# To get the net profit/loss, first take the difference between the profit/loss at each timepoints
for i in range((len(rows)-1)):
   change_list.append(int(rows[i+1][1]) - int(rows[i][1]))

# Initialize a change sum variable
total_change = 0

# Add all the profit/loss differenes from change_list
for k in range(len(change_list)):
    total_change += int(change_list[k])

# divide the sum of the differences by the total numner of differences
average_change = total_change / len(change_list)

# GREATEST PROFIT INCREASE

greatest_profit_increase = 0

for m in range(len(change_list)):
   if change_list[m] > greatest_profit_increase:
       greatest_profit_increase = change_list[m]

# GREATEST PROFIT LOSS

greatest_profit_loss = 0

for n in range(len(change_list)):
   if change_list[n] < greatest_profit_loss:
       greatest_profit_loss = change_list[n]


# print summary to terminal
print('------------------------------------------')
print('Financial Analysis')
print('------------------------------------------')
print(f'Total Months: {total_months}')
print('------------------------------------------')
print(f'Total: ${round(total_profit_loss,0)}')
print('------------------------------------------')
print(f'Average Change: ${round(average_change,2)}')
print('------------------------------------------')
print(f'Greatest Profit Increase: {rows[change_list.index(greatest_profit_increase)+1][0]} (${greatest_profit_increase})')
print(f'Greatest Profit Loss: {rows[change_list.index(greatest_profit_loss)+1][0]} (${greatest_profit_loss})') 
print('------------------------------------------')

# WRITE TEXT FILE

pypoll_file = open("pybank_data.txt","w") # w = write
pybank_file.write(f'Financial Analysis\nTotal Months: {total_months}\nTotal: ${round(total_profit_loss,0)}\nAverage Change: ${round(average_change,2)}\nGreatest Profit Increase: {rows[change_list.index(greatest_profit_increase)][0]}\nGreatest Profit Loss: {rows[change_list.index(greatest_profit_loss)][0]} (${greatest_profit_loss})')
pybank_file.close() 