# Dependencies
import os
import csv

# READ CSV

# first get the wd
dir_path = os.path.dirname(os.path.realpath(__file__)) # store the name of the wd
election_csvpath = os.path.join(dir_path, 'election_data.csv') # get the file fromthe current wd

# initalize lists of votes
votes_list = []
khan_list = []
correy_list = []
li_list = []
otooley_list = []
total_candidates = []

with open(election_csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

     # count the number of votes in total and for each candidate by making a list of votes cast
    for row in csvreader:
        votes_list.append(row[2])
        if row[2] == "Khan":
            khan_list.append(row[2])
        if row[2] == "Correy":
            correy_list.append(row[2])
        if row[2] == "Li":
            li_list.append(row[2])
        if row[2] == "O'Tooley":
            otooley_list.append(row[2])

# TOTAL VOTES CAST

total_votes = len(votes_list)

# TOTAL OF VOTES EACH CANDIDATE WON

# the length of each list is the number of votes because there is one row per vote    
khan_votes = len(khan_list)
correy_votes = len(correy_list)
li_votes = len(li_list)
otooley_votes = len(otooley_list)

# PERCENTAGE OF VOTES FOR EACH CANDIDATE

# The percentage is the candidate's votes divided by the total votes, multiplied by 100
khan_percentage = khan_votes / total_votes * 100
correy_percentage = correy_votes / total_votes * 100
li_percentage = li_votes / total_votes * 100
otooley_percentage = otooley_votes / total_votes * 100

# DECLARE THE WINNER

# create a dictionary with each candidate's name and the percentage of votes they won
candidate_dict = {'Khan': khan_percentage, 'Correy': correy_percentage, 'Li': li_percentage, 'OTooley': otooley_percentage}

# initalize a variable to hold the winner and their winning percentage of votes
winning_percentage = 0
winner = 'unknown'

# iterate through the dictionary to determine which candidate earned the highest percentage of votes
for key, value in candidate_dict.items():
    if value > winning_percentage:
        winning_percentage = value
        winner = key

# PRINT SUMMARY

print('Election Results')
print('------------------------------------------')
print(f'Total Votes: {total_votes}')
print('------------------------------------------')
print(f'Khan: {round(khan_percentage,3)}% ({khan_votes})')
print(f'Correy: {round(correy_percentage,3)}% ({correy_votes})')
print(f'Li: {round(li_percentage,3)}% ({li_votes})')
print(f'O\'Tooley: {round(otooley_percentage,3)}% ({otooley_votes})')
print('------------------------------------------')
print(f'Winner: {winner}')
print('------------------------------------------')

# WRITE TEXT FILE

pypoll_file = open("pypoll_data.txt","w") # w = write 
pypoll_file.write(f'Total Votes: {total_votes}\nKhan: {round(khan_percentage,3)}% ({khan_votes})\nCorrey: {round(correy_percentage,3)}% ({correy_votes})\nLi: {round(li_percentage,3)}% ({li_votes})\nO\'Tooley: {round(otooley_percentage,3)}% ({otooley_votes})\nWinner: {winner}')
pypoll_file.close() 