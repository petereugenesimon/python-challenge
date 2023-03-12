#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import os module to create file paths
import os

# Import module to read CSV files
import csv

# Set path for file
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Lists to store data
ballots = []
candidates = []

# Open CSV file
with open(election_data_csv) as election_file:
    # Variable to hold and deliminate file
    election_reader = csv.reader(election_file, delimiter=",")
    # Store header row
    election_header = next(election_reader)
    # Loop to add values
    for row in election_reader:
        ballots.append(row[0])
        candidates.append(row[2])

# Set variables for candidates names and vote counters
rad = "Raymon Anthony Doane"
rad_count = 0
dd = "Diana DeGette"
dd_count = 0
ccs = "Charles Casper Stockham"
ccs_count = 0

# Count total votes
total_votes = len(ballots)

# Loop through candidates and count votes
for vote in candidates:
    if vote == rad:
        rad_count = rad_count + 1
    elif vote == dd:
        dd_count = dd_count + 1
    elif vote == ccs:
        ccs_count = ccs_count + 1
        
# Calculate candidates' percentage of votes
rad_perc = (rad_count / total_votes) * 100
dd_perc = (dd_count / total_votes) * 100
ccs_perc = (ccs_count / total_votes) *100

# Create lists of candidates' names and votes
candidates_list = [rad, ccs, dd]
votes_list = [rad_count, ccs_count, dd_count]

# Calculate the winning amount
winning_amount = max(votes_list)

# Print election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# Round percentage to 3 decimals
print(f"{ccs}: {ccs_perc:.3f}% ({ccs_count})")
print(f"{dd}: {dd_perc:.3f}% ({dd_count})")
print(f"{rad}: {rad_perc:.3f}% ({rad_count})")
print("-------------------------")

# Zip candidate names and votes lists and find winning amount
results_zip = zip(candidates_list, votes_list)
for winner in results_zip:
    if winner[1] == winning_amount:
        print(f"Winner: {winner[0]}")
        
lines = ["Election Results", "-------------------------", f"Total Votes: {total_votes}", "-------------------------",
            f"{ccs}: {ccs_perc:.3f}% ({ccs_count})", f"{dd}: {dd_perc:.3f}% ({dd_count})", f"{rad}: {rad_perc:.3f}% ({rad_count})",
            "-------------------------", f"Winner: {winner[0]}"]

results_output = os.path.join('analysis', 'results.txt')

with open(results_output, 'w') as results_txt:
    results_txt.write('\n'.join(lines))


# In[ ]:




