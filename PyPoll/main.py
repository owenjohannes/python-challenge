import os
import csv

election_csv_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Open and read budget_csv
with open(election_csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# Read the header row first 
    csv_header = next(csv_reader)
    row_count = 0
    charles_votes = 0
    diana_votes = 0
    raymon_votes = 0
    winner_name = ''

    for row in csv_reader:
        
        # Count the total number of rows for total numbers of votes cast
        row_count = row_count + 1

        # Count the total number of votes for each candidate
        if row[2] == 'Charles Casper Stockham':
            charles_votes += 1
        elif row[2] == 'Diana DeGette':
            diana_votes += 1
        elif row[2] == 'Raymon Anthony Doane':
            raymon_votes += 1
        # Calculate the percentage of votes for each candidate
        total_votes = (charles_votes + diana_votes + raymon_votes)
        charles_percentage = charles_votes / total_votes * 100
        charles_percentage_str = "{:.3f}%".format(charles_percentage)
        diana_percentage = diana_votes / total_votes * 100
        diana_percentage_str = "{:.3f}%".format(diana_percentage)
        raymon_percentage = raymon_votes / total_votes * 100
        raymon_percentage_str = "{:.3f}%".format(raymon_percentage)
        # Print the winner of the election
        if charles_votes > diana_votes and charles_votes > raymon_votes:
            winner_name = 'Charles Casper Stockham'
        elif diana_votes > charles_votes and diana_votes > raymon_votes:
            winner_name = 'Diana DeGette'
        elif raymon_votes > charles_votes and raymon_votes > diana_votes:
            winner_name = 'Raymon Anthony Doane'
        else:
            winner_name = 'Tie'

# Print results of analysis on terminal as a test before writing file
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {row_count}')
print(f'-------------------------')
print(f'Charles Casper Stockham: {charles_percentage_str} ({charles_votes})')
print(f'Diana DeGette: {diana_percentage_str} ({diana_votes})')
print(f'Raymon Anthony Doane: {raymon_percentage_str} ({raymon_votes})')
print(f'-------------------------')
print(f'Winner: {winner_name}')
print(f'-------------------------')

# Open a file named 'pypoll_analysis.txt'
with open('PyPoll/analysis/pypoll_analysis.txt', 'w') as file:
    # Write the results of the analysis into the file
    file.write(f'Election Results\n')
    file.write(f'-------------------------\n')
    file.write(f'Total Votes: {row_count}\n')
    file.write(f'-------------------------\n')     
    file.write(f'Charles Casper Stockham: {charles_percentage_str} ({charles_votes})\n')
    file.write(f'Diana DeGette: {diana_percentage_str} ({diana_votes})\n') 
    file.write(f'Raymon Anthony Doane: {raymon_percentage_str} ({raymon_votes})\n')
    file.write(f'-------------------------\n')      
    file.write(f'Winner: {winner_name}\n')
    file.write(f'-------------------------\n')   