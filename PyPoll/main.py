import os
import csv
file_path = os.path.join('Resources','election_data.csv')

#declare variables and lists/disctionaries
total_votes = 0
votes_for_candidates = []
candidate_names = []
candidate_votes = []
candidate_percent = []
results = {}
percentage = {}

#create connection to file and read it
with open (file_path) as csv_file:
    info = csv.reader(csv_file, delimiter=',')
    first_row = next(info)

    #loop through to grab total votes/ who each vote was for/unique candidate list
    for row in info:
        total_votes = total_votes + 1
        current_candidate = row[2]
        votes_for_candidates.append(current_candidate)
        
        if current_candidate not in candidate_names:
            candidate_names.append(current_candidate)

    #pull a unique list of candidates   
    for name in votes_for_candidates:
        if name not in candidate_names:
            candidate_names.append(name)   

print('Election Results')
print('------------------')
print(f'Total Votes: {total_votes}')
print('------------------')

#create dictionary for candidate and their votes
for vote in votes_for_candidates:
    results[vote] = results.setdefault(vote,0) + 1
            
#create dictionary for candidate and their % of votes
for candidate in results:
    votes = results.get(candidate)
    percent = float(votes) / float(total_votes) * 100
    candidate_results = ( f"{candidate}: {percent:.1f}% ({votes:,})\n")
    print(candidate_results)

print('------------------')
#collect the winner based on largest vote count
find_max = max(results, key=results.get)
print('WINNER:', find_max)
print('------------------')        

#print to the txt file
output_file = os.path.join('Analysis', 'Output.txt')

with open (output_file,'a') as text_file:
    
    
    text_file.write('Election Results''\n') 
    text_file.write('------------------''\n')
    text_file.write(f'Total Votes: {total_votes}\n')
    text_file.write('------------------''\n')
            
    for candidate in results:
        votes = results.get(candidate)
        percent = float(votes) / float(total_votes) * 100
        #percentage[candidate] = round(percent,0)
        candidate_results = ( f"{candidate}: {percent:.1f}% ({votes:,})\n")
    
        text_file.write(candidate_results)

    text_file.write('------------------''\n')
    text_file.write(f'WINNER: {find_max}''\n')
    text_file.write('------------------')



