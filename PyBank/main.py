import os
import csv

budget_csv_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Open and read budget_csv
with open(budget_csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# Read the header row first 
    csv_header = next(csv_reader)

    row_count = 0
    total = 0
    total_sum = 0
    difference = 0
    previous_value = 0
    max_increase = 0
    max_decrease = 0
    date_max_increase = ""
    date_max_decrease = ""

    for row in csv_reader:
        
        # Count the total number of rows for total months
        row_count = row_count + 1
        
        # Count the total value of rows under Profit/Losses column
        total += int(row[1])
        
        # Count the total profit/losses
        current_value = int(row[1])
        if previous_value != 0:
            difference = current_value - previous_value
            total_sum += difference
            # Find the greatest increase in profits (date and amount)
            if difference > max_increase:
                max_increase = difference
                date_max_increase = row[0]
            # Find the greatest decrease in profits (date and amount)
            if difference < max_decrease:
                max_decrease = difference
                date_max_decrease = row[0]

        previous_value = current_value
  
# Count the average change of profit/losses
average_change = total_sum / (row_count - 1)
average_change_str = '{:.2f}'.format(average_change)

# Print results of analysis on terminal as a test before writing file
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total months: {row_count}")
print(f'Total: ${total}')
print(f'Average Change: ${average_change_str}')
print(f'Greatest Increase in Profits: {date_max_increase} (${max_increase})')
print(f'Greatest Decrease in Profits: {date_max_decrease} (${max_decrease})')

# Open a file named 'pybank_analysis.txt'
with open('PyBank/analysis/pybank_analysis.txt', 'w') as file:
    # Write the results of the analysis into the file
    file.write(f'Financial Analysis\n')
    file.write(f'----------------------------\n')
    file.write(f'Total months: {row_count}\n')
    file.write(f'Total: ${total}\n')       
    file.write(f'Average Change: ${average_change_str}\n')
    file.write(f'Greatest Increase in Profits: {date_max_increase} (${max_increase})\n')  
    file.write(f'Greatest Decrease in Profits: {date_max_decrease} (${max_decrease})\n')          