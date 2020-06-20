
# PyPoll_Challenge
#------------------------------------------------------------------------------------
# The data we need to retrieve.
# Adding dependencies
import csv
import os

#------------------------------------------------------------------------------------

# Defining Variables, Lists and Dictionaires to be used for later calculations

# Assigning a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assigning a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_results.txt")

# Initializing a total vote counter
total_votes = 0

# Creating an empty list for candidates
candidate_options = []

# Creating an empty list for counties
county_options =[]

# Creating an empty dictionary to hold number of votes for each candidate
candidate_votes = {}

# Creating an emoty dictionary to hold number of votes for each county
county_votes = {}

# Winning Candidate and Winning Count Tracker for Candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Winning County and Winning Count Tracker for County
winning_county =""
winning_county_count = 0
winning_county_percentage = 0

#------------------------------------------------------------------------------------

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

        county_name = row[1]
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        if county_name not in county_options:
            county_options.append(county_name)

            county_votes[county_name] = 0
        

        # Tallying the votes for each candidate
        candidate_votes[candidate_name] += 1

        # Tallying the votes for each county
        county_votes[county_name] += 1

#----------------------------------------------------------------------------------

# Writing results to text file and performing calcualtions for percentage of votes
# per county and candidate.  Compiling total votes for each candidate and county.
# Determining the county and candidate with the highest number of votes.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    #--------------------------------------------------------------------------------
    # Printing total votes in election in terminal and writing it to text file
    print(election_results, end="")
    txt_file.write(election_results)

    county_title = (f"\nCounty Votes:\n")
    print(county_title)
    txt_file.write(county_title)

    # ---------------------------------------------------------------------------------

    # Using for loop and if conditional to attain the percentage of votes for each
    # county and determining which county had the highest voter turnout
    for county in county_votes:
        cvotes = county_votes[county]
        county_vote_percentage = int(cvotes) / int(total_votes) * 100
        county_results = (f"{county}: {county_vote_percentage:.1f} % ({cvotes:,})\n")
        
        # Printing results to terminal and writing it to text file
        print(county_results)
        txt_file.write(county_results)
    
        if (cvotes > winning_county_count) and (county_vote_percentage > winning_county_percentage):
            winning_county_count = cvotes
            winning_county_percentage = county_vote_percentage
            winning_county = county

    winning_county_summary = (
        f"-----------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"------------------------------\n")

    # Printing county with the highest votes cast, writing results to text
    # file as well
    print(winning_county_summary)
    txt_file.write(winning_county_summary)

    #-------------------------------------------------------------------------------

    # Using for loop and if conditional to attain the percentage of votes for each
    # candidate and determining which candidate attained the highest number of votes
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f} % ({votes:,})\n")
        
        # Printing results to terminal and writing it to text file
        print(candidate_results)
        txt_file.write(candidate_results)
    
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f} %\n"
        f"---------------------------\n")
    
    # Printing candidate with the highest number of votes, writing results to text
    # file as well
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

#------------------------------------------------------------------------------------