import os
import csv

#Add pathway to an object
budget_db = os.path.join("Resources", "budget_data.csv")

#Defining Values and Lists
total_months = 0
total_profit_loss = 0
value = 0
change = 0
dates = []
profits = []

#Reading CSV file
with open(budget_db, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Read Header Row
    csv_header = next(csvreader)
    
    #Read FIRST_ROW to Set Up Analysis
    first_row = next(csvreader)
    total_months += 1
    total_profit_loss += int(first_row[1])
    value = int(first_row[1])
    
    #Cycle Through CSV File
    for row in csvreader:
        #Track DATES
        dates.append(row[0])
        #Calculate then Add CHANGE
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        #Add TOTAL_MONTHS
        total_months += 1
        #Calculate amount (net) Profit/Loss
        total_profit_loss = total_profit_loss + int(row[1])
    
    #Calculating Greatest Profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]
    
    #Calculating Greatest Loss (Decrease)
    greatest_decrease = min(profits)
    lowest_index = profits.index(greatest_decrease)
    lowest_date = dates[lowest_index]
    
    #Calculating Average Change in Profits/Losses
    average_change = sum(profits)/len(profits)

#Display Output
print("Financial Analysis")
print("__________________")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_profit_loss)}")
print(f"Average Change: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_decrease)})")

#Export File (.txt)
output = open("Budget.txt", "w")
line1 = "Financial Analysis"
line2 = "__________________"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_profit_loss)}")
line5 = str(f"Average Change: ${str(round(average_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_decrease)})")

output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))