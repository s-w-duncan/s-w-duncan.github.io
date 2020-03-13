import os
import csv

#Create Pathway to Object
election_db = os.path.join("Resources", "election_data.csv")

#Define Lists and Vote Counter
candidates = []
number_votes = []
percent_votes = []
votes_total = 0

#Open and Read Election Data
with open(election_db, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        votes_total += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.idex(row[2])
            number_votes.append(1)
            else:
                index = cadidates.index(row[2])
                number_votes = += 1
    for votes in number_votes:
        percentage = (votes/votes_total) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    winner = max(number_votes)
    index = number_votes.index(winner)
    candidate_elect = candidates[index]

print("Election Results")
print("________________")
print(f"Total Votes: {str(votes_total)}")
print("________________")
for x in range(len(candidates)):
    print(f"{candidates[x]}: {str(percent_votes[x]))} ({str(number_votes[x]))})")
print("________________")
print(f"Winner: {candidate_elect}")
print("________________")

output = open("ElectionResults.txt", "w")
line1 = "Election Results"
line2 = "________________"
line3 = str(f"Total Votes: {str(votes_total)}")
line4 = "________________"
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for x in range(len(candidates)):
    line = str(f"{candidates[x]}: {str(percent_votes[x]))} ({str(number_votes[x])})")
    output.writer('{}\n'.format(line))
line5 = "________________"
line6 = str(f"Winner: {candidate_elect}")
line7 = "________________"
output.writer('{}\n{}\n{}\n'.format(line5, line6, line7))