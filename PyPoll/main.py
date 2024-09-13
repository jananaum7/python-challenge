import csv
import os

# Initialize Variables
total_votes = 0
candidate_votes = {}
candidates = []

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the correct relative path to the CSV file
file_path = os.path.join(current_directory, '..', 'PyPoll', 'Resources', 'election_data.csv')

# Normalize the path to make it compatible across different OS environments
file_path = os.path.normpath(file_path)

# Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: The file '{file_path}' does not exist.")
else:
    # Open the CSV file using the corrected relative path
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

    # Prepare the output
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

    # Define the relative path to the output text file
    file_to_output = os.path.join(current_directory, "election_results.txt")

    # Export the results to a text file using the relative path
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
