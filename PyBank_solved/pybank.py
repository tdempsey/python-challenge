# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    total_months = 0
    total_pl = 0
    average_change = 0
    first_pl = 0
    greatest_increase_month =  ' '
    greatest_increase_pl = 0
    greatest_decrease_month =  ' '
    greatest_decrease_pl = 10000000000

    # Read each row of data after the header
    for row in csvreader:
        total_months += 1
        total_pl += int(row[1])

        if total_months == 1:
            first_pl = row[1]
            #print(first_pl)

        if int(row[1]) > int(greatest_increase_pl):
            greatest_increase_month =  row[0]
            greatest_increase_pl = row[1]

        if int(row[1]) < int( greatest_decrease_pl):
            greatest_decrease_month =  row[0]
            greatest_decrease_pl = row[1]

    average_change = (int(first_pl)-int(row[1]))
    
    print ("\nFinancial Analysis\n\n")
    print ("----------------------------\n\n")
    print ("Total Months: %d\n\n" % total_months)
    print ("Total: $%d\n\n" % total_pl)
    print ("Average Change: %d\n\n" % average_change)
    print ("Greatest Increase in Profits: %s ($%s)\n\n" % (greatest_increase_month, greatest_increase_pl))
    print ("Greatest Decrease in Profits: %s ($%s)\n\n" % (greatest_decrease_month, greatest_decrease_pl))

    with open('pybank.txt', 'w') as f:
        f.write ("Financial Analysis\n\n")
        f.write ("----------------------------\n\n")
        f.write ("Total Months: %d\n\n" % total_months)
        f.write ("Total: $%d\n\n" % total_pl)
        f.write ("Average Change: %d\n\n" % average_change)
        f.write ("Greatest Increase in Profits: %s ($%s)\n\n" % (greatest_increase_month, greatest_increase_pl))
        f.write ("Greatest Decrease in Profits: %s ($%s)\n\n" % (greatest_decrease_month, greatest_decrease_pl))


        
