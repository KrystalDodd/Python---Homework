
import os 
import csv

#Path
election_data = os.path.join(".\Resources\election_data.csv")
with open(election_data, 'r', encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csvheader = next(csvreader)
    #Variables
    total_votes = 0
    candidates = []
    votes = []
    total_votes_list = []
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        votes.append(candidate)
        if candidate not in candidates:
            candidates.append(candidate)
        total_votes += 1
    print("Election Results")
    print("-------------------------------------------------")
    print(total_votes)
    print("-------------------------------------------------")
    for candidate in candidates:
        count = 0
        for vote in votes:
            if candidate == vote:
                count = count + 1
        total_votes_list.append(count)
        vote_percentage = round(((count/total_votes)*100),2)
        print(candidate,count,vote_percentage)

    #Winner of Vote
    print("-------------------------------------------------")
    Highest_votes = max(total_votes_list)
    Index_of_winner = total_votes_list.index(Highest_votes)
    winner = candidates [Index_of_winner]
    print(f"Winner: {winner}")

    
   

    

         
   

    

    

