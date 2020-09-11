import os
import csv

# Path to collect data from the Resources folder
budgetdata_csv = os.path.join('Resources','budget_data.csv')

# Read csv file
with open(budgetdata_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip first title row 
    next(csvreader)
    profitloss = []
    date =[]
    profitloss_change=[]

    # Loop through rows and create list for profitloss and date 
    for row in csvreader:
        profitloss.append(float(row[1]))
        date.append(row[0])

    # Loop through values in profitloss list and create list for profitloss change by finding difference between one month and the next
    for i in range(1,len(profitloss)):

        profitloss_change.append(profitloss[i] - profitloss[i -1])

    #Find average of changes    
    averagechange = int(sum(profitloss_change) / len(profitloss_change))
    #Find max profitloss change
    maxaveragechange = int(max(profitloss_change))
    #Find min profitloss change
    minaveragechange = int(min(profitloss_change))
    #Find date when max profitloss change occurs
    maxaveragechangedate = str(date[profitloss_change.index(maxaveragechange)+1]) 
    #Find date when min profitloss change occurs
    minaveragechangedate = str(date[profitloss_change.index(minaveragechange)+1]) 

    #Output to text file
    outputtxt = open(os.path.join('analysis','analysis.txt'),"w")
    print("Financial Analysis", file= outputtxt)
    print("-----------------------", file= outputtxt)
    # Print count of all months by find lenth of data list
    print(f"Total Months: {len(date)}", file= outputtxt)
    # Print sum of total profit and loss
    print(f"Total: ${int(sum(profitloss))}", file= outputtxt)
    print(f"Average Change:${averagechange}", file= outputtxt)
    print(f"Greatest Increase in Profits: {maxaveragechangedate} (${maxaveragechange})", file= outputtxt)
    print(f"Greatest Decrease in Profits: {minaveragechangedate} (${minaveragechange})", file= outputtxt)
    outputtxt.close()

    #Print to terminal
    print("Financial Analysis")
    print("-----------------------")
    print(f"Total Months: {len(date)}")
    print(f"Total: ${int(sum(profitloss))}")
    print(f"Average Change:${averagechange}")
    print(f"Greatest Increase in Profits: {maxaveragechangedate} (${maxaveragechange})")
    print(f"Greatest Decrease in Profits: {minaveragechangedate} (${minaveragechange})")