#The data we need to retrieve
# Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
#create a file name variable to a direct path for saving
file_to_save = 'Analysis/election_analysis.txt'

#1. The total number of votes cast
total_votes = 0

#2. A complete list of candidates who received votes
#Declare a new list
candidate_options = []

# Declare the empty dictionary. 
candidate_votes = {}

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    
    #To do:read and perform analysis
    file_reader = csv.reader(election_data)
    
    # read and print the header row.
    headers = next(file_reader)
    
    #print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #find unique candidates
        if candidate_name not in candidate_options:
           
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidates vote count. Create each candidate as a key and set vote count to 0
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
   
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
           
        # If true then set winning_count = votes and winning_percent = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage

        # Set the winning candidate equal to the candidate's name
        winning_candidate = candidate_name

# To do: print out the winning candidate, vote count and percentage to terminal
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Close the file




#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

