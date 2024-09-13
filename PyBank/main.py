import os
import csv

# Set the current working directory to where your script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Initialize the variables
total_months = 0
net_total = 0
changes = []
dates = []
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

# Define the correct relative path to the CSV file
csv_file_path = os.path.join(current_directory, 'Resources', 'budget_data.csv')

try:
    # Open the CSV file using the correct relative path
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row

        prev_profit = None  # Initialize prev_profit to None

        for row in csv_reader:
            total_months += 1
            net_total += int(row[1])
            dates.append(row[0])

            # Calculate changes in profit/losses
            if prev_profit is not None:
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
    if len(changes) > 0:
        average_change = sum(changes) / len(changes)
    else:
        average_change = 0  # Handle division by zero if there are no changes

    # Prepare the output
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
    )

    # Print the output (to terminal)
    print(output)

    # Export the results to a text file
    file_to_output = os.path.join(current_directory, "budget_analysis.txt")
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
