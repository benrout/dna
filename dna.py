from sys import argv, exit
import csv
import re

# Check if correct number of command line arguments
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit()

# Initialise dictionary of STRs
strs = {}

# Initialise database of people
database = []

# Open csv file (data)
with open(argv[1]) as data_file:
    csv_reader = csv.DictReader(data_file)
    # Loop through each row in csv file and add to append to database
    for row in csv_reader:
        database.append(row)

    # Read STRs from first line of csv into STRs dictionary and set value/count to 0
    for i in range(1, len(csv_reader.fieldnames)):
        strs[csv_reader.fieldnames[i]] = 0

# Open text file (sequence)
with open(argv[2]) as text_file:
    # Read text file into sequence variable
    sequence = text_file.read()

# Loop through each STR
for str in strs:
    # Regex to find STR repeated one or more times
    regex = f"(?:{str})+"
    matches = re.findall(regex, sequence)

    # Initialise longest_match to zero
    longest_match = 0

    # Loop through all matches
    for match in matches:
        # Calculate how many times STR is repeated
        match_length = int(len(match)/len(str))

        # If match is longer than current longest match
        if match_length > longest_match:
            # Update longest match to current match length
            longest_match = match_length

    # Update STRs dictionary with longest match
    strs[str] = longest_match

# Search database for matching DNA
for person in database:
    # Initialise count for how many STRs match
    count = 0

    # Loop through each STR
    for str in strs:
        # If person has different amount of STR then break and go to next person
        if int(person[str]) != strs[str]:
            break

        # Increment count of STR matches
        count += 1

        # If person matches for all STRs
        if (count == len(strs)):
            print(person['name'])
            exit()

print("No match")