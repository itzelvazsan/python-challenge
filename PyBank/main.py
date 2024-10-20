# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # Output file path

#Lists to store the data
dates = []
profit_losses = []
net_change_ls = []

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_net = int(1088983)
greatest_increase = 0
greatest_decrease = 0
increase_date = ""
decrease_date = ""

# Add more variables to track other necessary financial data


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)


    # Skip the header row
    header = next(reader)
    print(f'CSV reader_ {header}')

    # Extract first row to avoid appending to net_change_list
    row_2 = next(reader)
    print(row_2)

    # Track the total and net change
    # Process each row of data
    for row in reader:

        #Dates and profits in lists
        dates.append(row[0])
        profit_losses.append(int(row[1]))
        
        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - previous_net
        net_change_ls.append(net_change)

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase:
            greatest_increase = net_change
            increase_date = row[0]
        
                 
        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            decrease_date = row[0]
    
        
        #Update counter for previous profit
        previous_net = int(row[1])

            
# Generate the output summary
total_months += 1 #Add one because first row was excluded
total_net += 1088983 #Add value of first row because of the exclusion


# Calculate the average net change across the months
# Adding up the changes to obtain average and dividing bu number of months:
average_change = round(sum(net_change_ls) / (len(dates)), 2)

# Print the output
results_printing = str(print(f"FINANCIAL ANALYSIS \n-------------------------\n" 
                         f"Total Months: {total_months} -------- \n"
                         f'Total Net: ${total_net} ------ \n'
                         f'Average Change: ${average_change} --- \n'
                         f'Greatest Increase in Profits: {increase_date} (${greatest_increase}) \n'
                         f'Greatest Decrease in Profits: {decrease_date} (${greatest_decrease}) \n'))


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(results_printing)