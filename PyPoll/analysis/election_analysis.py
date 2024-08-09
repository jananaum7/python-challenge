# Modules
import csv
import os

# Initialize Variables
total_votes = 0
candidate_votes = {}
candidates = []

# Open the CSV file
file_path = 'C:/Users/tasee/OneDrive/Desktop/bootcamp/DATA-PT-EAST-JULY-071524/Homework/03-Python/python-challenge/Starter_Code/PyPoll/Resources/election_data.csv'
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Calculate vote percentages
vote_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Exporting file into a text file
file_to_output = "election_results.txt"
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
for candidate in candidates:
    output += f"{candidate}: {vote_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n"
output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print the output (to terminal)
print(output)

# Export the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)