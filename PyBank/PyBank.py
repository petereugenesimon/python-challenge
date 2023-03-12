#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import os module to create file paths
import os

# Import module to read CSV files
import csv

# Import module to help with calculating monthly changes
import numpy

# Set path for file
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Lists to store data
months = []
pls = []
    
# Open CSV file
with open(budget_data_csv) as budget_file:
    # Variable to hold file and deliminate file
    budget_reader = csv.reader(budget_file, delimiter=",")
    # Store header row
    budget_header = next(budget_reader)
    # Loop to add values
    for row in budget_reader:
        # Add months
        months.append(row[0])
        # Add profits/losses
        pls.append(row[1])
            
# Convert profits/losses from string to integer
pls = [int(i) for i in pls]
    
# Count total months
total_months = len(months)
    
# Sum total profits/losses
total_pls = sum(pls)
    
# Calculate monthly changes
changes = numpy.diff(pls)
    
# Convert monthly changes array to list
rev_changes = list(changes)
    
# Insert beginning value to monthly changes list to have same length as months list
rev_changes.insert(0, 0)
    
# Sum total monthly changes
total_changes = sum(rev_changes)
    
# Calculate average monthly changes
average_changes = total_changes / (total_months - 1)
    
# Calculate greatest profit
max_change = max(changes)
    
# Calculate greateast loss
min_change = min(changes)

# Print financial analysis statement
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_pls}")
# Round average change to 2 decimals
print(f"Average Change: ${average_changes:.2f}")
    
# Zip months and changes list and find row with greatest profit
changes_zip = zip(months, rev_changes)
for maxrow in changes_zip:
        if maxrow[1] == max_change:
            print(f"Greatest Increase in Profits: {maxrow[0]} (${max_change})")

# Zip months and changes list and find row with greatest loss
changes_zip = zip(months, rev_changes)
for minrow in changes_zip:
        if minrow[1] == min_change:
            print(f"Greatest Decrease in Profits: {minrow[0]} (${min_change})")
            
lines = ["Financial Analysis", "----------------------------", f"Total Months: {total_months}", f"Total: ${total_pls}", 
            f"Average Change: ${average_changes:.2f}", f"Greatest Increase in Profits: {maxrow[0]} (${max_change})",
             f"Greatest Decrease in Profits: {minrow[0]} (${min_change})"]

analysis_output = os.path.join('analysis', 'analysis.txt')

with open(analysis_output, 'w') as analysis_txt:
    analysis_txt.write('\n'.join(lines))


# In[ ]:




