# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who reveived votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.


# Adding dependencies
import csv

import os

# Assigning a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assigning a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Opening and reading election results file
with open(file_to_load) as election_data:

    # Reading and analyzing data with reader function
    file_reader = csv.reader(election_data)


    # Read and print the header row
    headers = next(file_reader)
    print(headers)






