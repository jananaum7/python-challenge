# Modules
import csv

# Initialize the variables 
total_months = 0
net_total = 0 
changes = []
dates = []
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

# Open the CSV file
with open('C:/Users/tasee/OneDrive/Desktop/bootcamp/DATA-PT-EAST-JULY-071524/Homework/03-Python/Starter_Code/PyBank/Resources/budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        total_months += 1
        net_total += int(row[1])
        dates.append(row[0])

        # Calculate changes in profit/losses
        if total_months > 1:
            change = int(row[1]) - int(prev_profit)
            changes.append(change)

         # Find greatest increase and decrease
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        prev_profit = row[1]
# Calculate the average change
average_change = sum(changes) / len(changes)

# Print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")