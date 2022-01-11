import os
import csv
Pypoll_csv = os.path.join( ".." , "Resources" , "election_data.csv")
count = 0
voterlist = []
distinct_voter = []
vote_count = []
vote_percent = []
with open(Pypoll_csv , newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        count = count + 1
        voterlist.append(row[2])
        for part in set(voterlist):
            distinct_voter.append(part)
            ballot = voterlist.count(part)
            vote_count.append(ballot)
            chance = (ballot/count) * 100
            vote_percent.append(chance)
        winning_vote_count = max(vote_count)
        winner = distinct_voter[vote_count.index(winning_vote_count)]

print("--------------------------------------")
print("Election Results")
print("--------------------------------------")
print("Total Votes :" + str(count))
print("--------------------------------------")
for k in range(len(distinct_voter)):
    print(distinct_voter[k]) + ":" + str(vote_percent[k]) +"% (" +str(vote_count[k]+ ")")
    print("----------------------------------")
    print("The winner is: " + winner)
    print("----------------------------------")

with open("election_results.txt" , "w") as text:
     text.write("--------------------------------------")
     text.write("Election Results")
     text.write("--------------------------------------")
     text.write("Total Votes :" + str(count))
     text.write("--------------------------------------")
     for k in range(len(distinct_voter)):
         text.write(distinct_voter[k]) + ":" + str(vote_percent[k]) +"% (" +str(vote_count[k]+ ")")
     text.write("----------------------------------")
     text.write("The winner is: " + winner)
     text.write("----------------------------------")
