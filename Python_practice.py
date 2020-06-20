# Testing Python
print("Hello World!")


# Practice Conditionals
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])
    

# Membership Operators
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties")
else:
    print("Arapahoe is in the list counties and El Paso is not in the list of counties")


# For loops
for county in counties:
    print(county)


# For loop with built-in function range()
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)


# For loop using range() function
for num in range(5):
    print(num)


# Using indexing to iterate through a list
for i in range(len(counties)):
    print(counties[i])


# Iterate through dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)


# Iterate through dictionary to print keys
for county in counties_dict.keys():
    print(county)


# Iterate through dictionary to print values with dictionary_name [key] format
for county in counties_dict:
    print(counties_dict[county])


# Iterate through dictionary to print values using get() method
for county in counties_dict:
    print(counties_dict.get(county))


# Iterate through dictionary to print values
for voters in counties_dict.values():
    print(voters)


# Iterate through dictionary to print items
for items in counties_dict.items():
    print(items)


# Iterate through dictionary to print key-value pairs
for county, voters in counties_dict.items():
    print(county, voters)


# Iterate through dictionary to print key-value pairs with text
for county, voters in counties_dict.items():
    print(county, "county has" , voters, "registered voters.")


# Searching for a dictionary within a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


# Using range() function to iterate over the list
for i in range(len(voting_data)):
    print(voting_data[i])

# Using nested for loop to print values from list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# Retrieving only the number of registered voters from list of dictionaries
for county_dict in voting_data:
    print(county_dict["registered_voters"])


# Retrieving only the county from the list of dictionaries
for county_dict in voting_data:
    print(county_dict["county"])


# Printing with f-strings
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
print(f"I received {my_votes/total_votes * 100}% of the total votes.")

# Using f-strings with dictionaries
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} voters.")

# Multiple f-strings
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f"The totalnumber of votes in the election was {total_votes}."
    f"You received {candidate_votes/total_votes * 100}% of the total votes."
)

print(message_to_candidate)


# Formatting Floating-Point Decimals (f"{value:{width},.{precision}}")
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f"The totalnumber of votes in the election was {total_votes}."
    f"You received {candidate_votes/total_votes * 100:.2f}% of the total votes."
)

print(message_to_candidate)

# Skill drill f-strings
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters.")


 
# Using datetime module to tell us the current time
import datetime
now = datetime.datetime.now()
print("The time right now is", now)

# Eliminating confusion with datetime module
import datetime as dt
now = dt.datetime.now()
print("The time right now is", now)







