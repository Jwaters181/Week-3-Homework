import os
import csv
pybank_csv = os.path.join(".." , "Resources" , "budget_data.csv")
profit =[]
monthly_changes =[]
date =[]
count = 0
Total_profit = 0
Total_change_profits = 0
starting_profit = 0
with open(pybank_csv , newline = "") as csvfile:
    pycsvreader = csv.reader(csvfile, delimiter = ",")
    pyheader = next(pycsvreader)
    for row in pycsvreader:
        count = count + 1
        date.append(row[0])
        profit.append(row[1])
        Total_proft = Total_profit + int(row[1])
        calculated_profit = int(row[1])
        monthly_change_profits = calculated_profit - starting_profit
        monthly_changes.append(monthly_change_profits)
        Total_change_profits = Total_change_profits + monthly_change_profits
        starting_profit = calculated_profit
        average_change_profits = (Total_change_profits/count)
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)
        date_increase = date[monthly_changes.index(greatest_increase_profits)]
        date_decrease = date[monthly_changes.index(greatest_decrease_profits)]
        print('------------------------------------------------------------')
        print("Financial Analysis")
        print("------------------------------------------------------------")
        print("Total Months:" + str(count))
        print("Total Profits:" + "$" + str(Total_profit))
        print("Average Change:" + "$" + str(int(average_change_profits)))
        print("Greatest Increase in Profits:" + str(date_increase) + " ($" + str(greatest_increase_profits) + ")")
        print("Greatest Decrease in Profits:" + str(date_decrease) + " ($" + str(greatest_decrease_profits) + ")")
        print("-------------------------------------------------------------")

        with open("budget_data.txt" , 'w') as text:
            text.write("--------------------------------------------")
            text.write("Financial Analysis" + "\n")
            text.write("--------------------------------------------")
            text.write("Total Months" + str(count))
            text.write("Total Profits:" + "$" + str(count))
            text.write("Average Change:" + "$" + str(int(average_change_profits)))
            text.write("Greatest Increase in Profits:" + str(date_increase) + " ($" + str(greatest_increase_profits) + ")")
            text.write("Greatest Decrease in Profits:" + str(date_decrease) + " ($" + str(greatest_decrease_profits) + ")")
            



    



