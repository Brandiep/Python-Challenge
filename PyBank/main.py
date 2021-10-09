import os
import csv

#find the file we want to read
file_path = os.path.join('Resources', 'budget_data.csv')

#declare everything before connecting to file
total_months = 0
past_total = 0
net_profits_loss = 0
greatest_increase = 0
greatest_decrease = 0
#create empty list to store data
total_change = []
date = []

#open file in read mode- gives access
with open (file_path) as csvfile:
    info = csv.reader(csvfile, delimiter=',')
#next is a step down/drop to next row-we dont need to header details
    first_row = next(info)
    #loop through data
    for row in info:  
        #number of rows equals number of months
        total_months = total_months + 1
        #find change in price
        current_total = (int(row[1]))
        change = current_total - past_total
        total_change.append(change)
        past_total = current_total
        date.append(row[0])
        #calculate net profit/net_profit_loss
        net_profits_loss = net_profits_loss + current_total

max_value = max(total_change)
max_value_index = total_change.index(max_value)
greatest_change_month = date[max_value_index]

min_value = min(total_change)
min_value_index = total_change.index(min_value)
smallest_change_month = date[min_value_index]

average_change = round(sum(total_change)/len(total_change),2)

print('Financial Analysis')
print('------------------')
print(f'Total Months: {total_months}')
print(f'Average Change: $ {average_change}')
print(f'Total: $ {net_profits_loss}')
print(f'Greatest Increase in Profits: {greatest_change_month} $ {max_value}')
print(f'Greatest decrease in Profits: {smallest_change_month} $ {min_value}')

output_file = os.path.join('Analysis', 'Output.txt')

with open (output_file,'a') as text_file:
    text_file.write('Financial Analysis''\n') 
    text_file.write('------------------''\n')
    text_file.write(f'Total Months: {total_months}''\n')
    text_file.write(f'Average Change: $ {average_change}''\n')
    text_file.write(f'Total: $ {net_profits_loss}''\n')
    text_file.write(f'Greatest Increase in Profits: {greatest_change_month} $ {max_value}''\n')
    text_file.write(f'Greatest decrease in Profits: {smallest_change_month} $ {min_value}') 