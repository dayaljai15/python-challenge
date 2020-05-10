import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next[csvreader]


    #each row read as a row
    for row in csvreader:
        print(row)

        
    # Number of months in file

    row_count = sum(1 for row in csvreader)
    next(csvreader)


    print ("Financial Analysis")
    print (f"Total Months : {row_count}")


    # The net total amount of "Profit/Losses" over the entire period

    month_of_change = []
    sum_loss = 0
    totalPl = 0
    income_change = 0
    sum_profit = 0
    profit = 0
    greatest_profit_increase = [" ", 0]
    greatest_profit_loss = [" ", 1000000]

    for row in csvreader:
        profit = int(row[1])
        if profit > 0:
            sum_profit = sum_profit + profit
        elif profit < 0:
            sum _loss = sum_loss + profit
    totalPl = sum_profit - sum_loss
    print (f"Total : {totalPl}")

    #The average of the changes in "Profit/Losses" over the entire period


    income_change = int(row["Profit/Losses"])- previous_income
    previous_income = int(row["Profit/Losses"])
    income_change_list = income_change_list + [income_change]
     month_of_change = [month_of_change] + [row["Date"]]
       




    #The greatest increase in profits (date and amount) over the entire period

    if income_change>greatest_increase[1]:
            greatest_increase[1]= income_change
            greatest_increase[0] = row['Date']

    

    #The greatest decrease in losses (date and amount) over the entire period

    if income_change<greatest_decrease[1]:
            greatest_decrease[1]= income_change
            greatest_decrease[0] = row['Date']
    income_average = sum(income_change_list)/len(income_change_list)


