# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output = open("Pypoll.txt","w")


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Declare Variables
    votes_cast = 0
    total_votes_cast = 0
    candidates = []
    candidates_won = {}
    candidates_won_percent = 0
    winner_name = " "
    winner_votes = 0
  
    # Read each row of data after the header
    for row in csvreader:
        votes_cast +=1
    
        #calculate unique list and candidates and calculate votes for each
        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_won[row[2]]=0

        candidates_won[row[2]]+=1

    print (candidates_won)
    
    print("\nElection Results\n\n")
    print("-------------------------\n\n")
    print(f"Total Votes: {votes_cast}\n\n")
    print("-------------------------\n\n")

    #print percentage of votes each candidate won
    for name in candidates_won:
        votes = candidates_won[name]
        percentage = votes / votes_cast
        pretty = percentage * 100
        print(f"{name}: {pretty:.3f}% ({votes})")
        output.write(f"{name}: {pretty:.3f}% ({votes}\n\n")

    #print the winner of the election based on popular vote
        if votes > winner_votes: 
            winner_votes = votes
            winner_name = name

    #write results to a text file
    print("\n-------------------------\n\n")
    print(f"Winner: {winner_name}\n\n")
    print("-------------------------\n\n")

    output.write("Election Results\n")
    output.write("-------------------------\n\n")
    output.write("Total Votes: {votes_cast}\n")
    output.write("-------------------------\n")
    output.write("-------------------------\n\n")
    output.write(f"Winner: {winner_name}\n\n")
    output.write("-------------------------\n")
