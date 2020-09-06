import os
import csv

# Path to collect data from the Resources folder
electiondata_csv = os.path.join('PyPoll','Resources','election_data.csv')

# Read csv file
with open(electiondata_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip first title row and open empty lists of all votes
    next (csvreader)
    votes = []
    
    # Loop through rows to output votes in votes list
    for row in csvreader:
        votes.append(str(row[2]))

# Open dictionary to votes and votes count
votesdict = {}
votesdictpercent = {}

# Run loop which goes through votes in votes list. If the canditate's name is in list then add 1, if it is not then start at 1
for canditates in votes:
    if canditates in votesdict:
        votesdict[canditates] += 1
    else:
        votesdict[canditates] = 1

# Find total votes by summing number of votes per canditate in votes dictionary 
totalvotes = sum(votesdict.values())
# Find who got the most gets by finding the max value in dictionary and the corresponding canditate(key)
mostvotes = max(votesdict, key=votesdict.get)

# Create new dictionary to equate percentage of votes using votesdict dictionary copy
votesdictpercent = dict(votesdict)

for percent in votesdictpercent:
    votesdictpercent[percent] = round(((votesdictpercent[percent] / totalvotes)*100),3)

# Get around F-string apostrophe error with O'Tooley
tooleyvotes= votesdict["O'Tooley"]
tooleypercent= votesdictpercent["O'Tooley"]

#Output to text file
outputtxt = open(os.path.join('PyPoll','analysis','analysis.txt'),"w")
print("Election Results", file= outputtxt)
print("---------------------------", file= outputtxt)
print(f'Total Votes: {totalvotes}', file= outputtxt)
print("---------------------------", file= outputtxt)
print(f'Khan: {votesdictpercent["Khan"]}% ({votesdict["Khan"]})', file= outputtxt)
print(f'Correy: {votesdictpercent["Correy"]}% ({votesdict["Correy"]})', file= outputtxt)
print(f'Li: {votesdictpercent["Li"]}% ({votesdict["Li"]})', file= outputtxt)
print(f'O\'Tooley: {tooleypercent}% ({tooleyvotes})', file= outputtxt)
print("---------------------------", file= outputtxt)
print(f'Winner: {mostvotes}', file= outputtxt)
print("---------------------------", file= outputtxt)
outputtxt.close()

#Print to terminal
print("Election Results")
print("---------------------------")
print(f'Total Votes: {totalvotes}')
print("---------------------------")
print(f'Khan: {votesdictpercent["Khan"]}% ({votesdict["Khan"]})')
print(f'Correy: {votesdictpercent["Correy"]}% ({votesdict["Correy"]})')
print(f'Li: {votesdictpercent["Li"]}% ({votesdict["Li"]})')
print(f'O\'Tooley: {tooleypercent}% ({tooleyvotes})')
print("---------------------------")
print(f'Winner: {mostvotes}')
print("---------------------------")