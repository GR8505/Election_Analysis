
# The data we need to retrieve.
# Adding dependencies
import csv

import os

# Assigning a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assigning a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")


# Initializing a total vote counter
total_votes = 0

# Creating empty list for candidates
candidate_options = []

# Creating an empty dictionary to hold number of votes for each candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Opening and reading election results file
with open(file_to_load) as election_data:

    # Reading and analyzing data with reader function
    file_reader = csv.reader(election_data)


    # Read the header row
    headers = next(file_reader)
    
    # Printing each row in the csv file
    for row in file_reader:
        
        # Adding to the total vote count
        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        # Tallying the votes for each candidate
        candidate_votes[candidate_name] += 1

# Writing results to text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # 1. The total number of votes cast
    # Printing the total votes
    print(f"Total number of votes cast = {total_votes}")


    # 2. A complete list of candidates who reveived votes
    # Printing candidate list
    print(f"List of candidates\n-----------------")
    for candidate in candidate_options:
        print(f"{candidate}\n")


    # 3. The percentage of votes each candidate won
    # 4. The total number of votes each candidate won
    # Calculating the percentage of votes for each candidate
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f} % ({votes:,})\n")
        print(candidate_results)
    
        txt_file.write(candidate_results)
    
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    

    # 5. The winner of the election based on popular vote.
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f} %\n"
        f"---------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
