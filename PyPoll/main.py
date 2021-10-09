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
#votes = 0
#create connection to file and read it
with open (file_path) as csv_file:
    info = csv.reader(csv_file, delimiter=',')
    first_row = next(info)

    #loop through to grab total votes, who each vote was for, and create dictionary
    for row in info:
        total_votes = total_votes + 1
        current_candidate = row[2]
        votes_for_candidates.append(current_candidate)
        
        if current_candidate not in candidate_names:
            candidate_names.append(current_candidate)


        #if x in candidate_names == current_candidate:
            #votes =  votes + 1
            #candidate_votes.append(votes)              
        #candidate_votes[candidate_name] = candidate_votes[candidate_names] + 1
        #for vote in votes_for_candidates:
            #cound times each candidates name voted
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
    #print(vote)
    results[vote] = results.setdefault(vote,0) + 1
    #print(results)        
#create dictionary for candidate and their % of votes
for candidate in results:
    votes = results.get(candidate)
    percent = float(votes) / float(total_votes) * 100
        #percentage[candidate] = round(percent,0)
    candidate_results = ( f"{candidate}: {percent:.1f}% ({votes:,})\n")
    print(candidate_results)

print('------------------')

find_max = max(results, key=results.get)
print('WINNER:', find_max)


print('------------------')        
#print('Election Results')
#print('------------------')
#print(f'Total Votes: {total_votes}')
#print('------------------')

#for key,value in percentage.items():
    #print(key, ':', value, '%')
#

#print(f'{candidate_names[0]}:)
#print(f'Winner: ')

#print(candidate_names)
#print('------------------')
#print(percentage)
#print(results)

output_file = os.path.join('Analysis', 'Output.txt')

with open (output_file,'a') as text_file:
    
    
    text_file.write('Election Results''\n') 
    text_file.write('------------------''\n')
    text_file.write(f'Total Votes: {total_votes}\n')
    text_file.write('------------------''\n')
    #for vote in votes_for_candidates:
    #print(vote)
        #results[vote] = results.setdefault(vote,0) + 1
            
#create dictionary for candidate and their % of votes
    for candidate in results:
        votes = results.get(candidate)
        percent = float(votes) / float(total_votes) * 100
        #percentage[candidate] = round(percent,0)
        candidate_results = ( f"{candidate}: {percent:.1f}% ({votes:,})\n")
    
        text_file.write(candidate_results)

    text_file.write('------------------''\n')
    text_file.write(f'WINNER: {find_max}''\n')
    text_file.write('------------------')



