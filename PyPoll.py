#The data we need to retrieve
# Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
#create a file name variable to a direct path for saving
file_to_save = 'Analysis/election_analysis.txt'
# Open the election results and read the file. 
with open(file_to_load) as election_data:
    #To do:read and perform analysis
    file_reader = csv.reader(election_data)
    # read and print the header row.
    headers = next(file_reader)
    print(headers)
# Close the file

#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

