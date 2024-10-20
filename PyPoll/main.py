# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
cand_1 = 0
cand_2 = 0
cand_3 = 0

# Winning Candidate and Winning Count Tracker
winner = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row & If the candidate is not already in the candidate list, add them
        if row[2] not in candidates:
            candidates.append(row[2])

        # Add a vote to the candidate's count
        if row[2] == 'Charles Casper Stockham':
            cand_1 += 1

        if row[2] == 'Diana DeGette':
            cand_2 += 1

        if row[2] == 'Raymon Anthony Doane':
            cand_3 += 1

# Get the vote count and calculate the percentage
#Generate dictionary of candidates counts and percentages
cand_1_percentage = round((cand_1 / total_votes) * 100, 3)
cand_2_percentage = round((cand_2 / total_votes) * 100, 3)
cand_3_percentage = round((cand_3 / total_votes) * 100, 3)

candidates_count = {candidates[0]: [cand_1, cand_1_percentage], candidates[1]: [cand_2, cand_2_percentage], candidates[2]: [cand_3, cand_3_percentage]}

# Update the winning candidate if this one has more votes
# Loop through the candidates to determine vote percentages and identify the winner
if cand_1 > 0:
    winner = candidates[0]

if cand_2 > cand_1:
    winner = candidates[1]

if cand_3 > cand_2:
    winner = candidates[2]

# Print and save each candidate's vote count and percentage
# Generate and print the winning candidate summary
election_results = (
    f"ELECTION RESULTS \n-------------------------\n" 
    f"Total Votes: {total_votes} \n"
    f"\n-------------------------\n"
    f'{candidates[0]}: {cand_1_percentage}% ({cand_1} votes) \n'
    f'{candidates[1]}: {cand_2_percentage}% ({cand_2} votes) \n'
    f'{candidates[2]}: {cand_3_percentage}% ({cand_3} votes) \n'
    f"\n-------------------------\n"
    f'Winner: {winner} \n'
    f"\n-------------------------\n")

print(election_results)

# Save the winning candidate summary to the text file
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(election_results)