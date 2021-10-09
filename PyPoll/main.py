import os
import csv
file_path = os.path.join('Resources','election_data.csv')

total_votes = 0
votes_for_candidates = []
candidate_names = []
results = {}

with open (file_path) as csv_file:
    info = csv.reader(csv_file, delimiter=',')
    first_row = next(info)

    for row in info:
        total_votes = total_votes + 1
        current_candidate = row[2]
        votes_for_candidates.append(current_candidate)

#pull a unique list of candidates
for name in votes_for_candidates:
    if name not in candidate_names:
            candidate_names.append(name)

for vote in votes_for_candidates:
    results[vote] = results.setdefault(vote,0) + 1


print(total_votes)
print(candidate_names)
print(results)



#instead of using specific name, try grabbng the info with a list - incase the file changes (candidate names or ore added)
#can use a key and name in a dictionary
#create an emply list to loop through and find candidates(like finding a ticker)
    #would need an if statement
    #at same time we grab the candidate name, we can set it to 0 to hold number of votes
#can1 = "Khan"
#can2 = "Correy"



