import os
import csv
from collections import Counter
csv_file = os.path.join("election_data.csv")  
with open (csv_file) as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csvreader)
    counter = 0
    all_votes = [] 
    d = {} 
    for row in csvreader:
        counter = counter + 1
        all_votes.append(row[2])

    total_votes = int(len(all_votes))
    d["total votes"]= total_votes
    candidate_list = []
    for word in all_votes:
        if word not in candidate_list:
            candidate_list.append(word)
       
    #d = Counter(candidate_list)
    
    all_votes = sorted(all_votes)
    last_value = len(all_votes) - 1 
    print("election results")  
    print(f"total votes: {total_votes}")
    vote_counts = 0
    greatest_value = 0
    
    for a, b in zip(all_votes, all_votes[1:]):
        if a == b:
            vote_counts = vote_counts + 1
        elif a != b:
            vote_counts = vote_counts + 1      
            precentage_votes = round(((vote_counts/total_votes)*100),2)
            if vote_counts > greatest_value:
                greatest_value = vote_counts
                winner = a
            
            candidate_name = a 
            d[a]= [vote_counts,precentage_votes]
            print(f"{candidate_name}: {precentage_votes}% ({vote_counts})")
            
            vote_counts = 0
    precentage_votes = round(((vote_counts/total_votes)*100),2) 
    d[a] = [(vote_counts + 1), precentage_votes]   
    candidate_name = a 
    
    print(f"{candidate_name}: {precentage_votes}% ({vote_counts})")
    
    print(f"winner: {winner}")
    d["winner"]= winner


output_path = os.path.join("results","pypoll_results.csv")
with open(output_path, "w", newline= '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter =',')
   
  
    csvwriter.writerow(["Election Results", " "])    
    csvwriter.writerow(["Candidate name", " presentage of votes ","number of votes"])  
    for key, value in d.items():
        csvwriter.writerow([key, value])






