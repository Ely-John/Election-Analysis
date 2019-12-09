# Add our dependencies.
import csv
import os


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, winning county and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#How many votes does each county got?
total_county_votes = 0
#getting the number for county's biggest turnout
county_largest_turnout= ""

# Initialize a total vote counter.
total_votes = 0
total_county_votes= 0

winning_county= ""
winning_county_percentage = 0
winning_county_votes= 0
# Candidate options and candidate votes
counties = []
# 1. Declare the empty dictionary.
counties_dict = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)
   
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1 
        total_county_votes += 1

        
        # Print the counties name from each row.
        county_name = row[1]

        if county_name not in counties:
          # Add the county name to the candidate list.
            counties.append(county_name)

           # 2. Begin tracking that candidate's vote count. 
            counties_dict[county_name] = 0

# to remove the code ...print(counties_dict)

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

   
#Checking the counties turnout

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(election_data)

    for row in file_reader:
        total_county_votes +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    #Calculating voter turnout results
    
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)
        
#Designing the output
with open(file_to_load) as county_votes:
    file_reader = csv.reader(county_votes)
    headers = next(county_votes)

for county in counties_dict:
       county_votes= counties_dict[county]
       county_votes_percentage= float(county_votes)/ float(total_votes) * 100
       
       #the results
       counties_results=(
           f"{county}:{county_votes_percentage:.1f}% {county_votes: ,}\n"
       )
       print(counties_results)
# Save the final county vote to the text file
txt.file.write(counties_results)   


#to count the votes each county recieved

if (county_votes>winning_county_votes) and (county_vote_percentage > winning_county_percentage):

     winning_coounty= county
     winning_county_votes= county_vote
     winning_county_percentage =county_vote_percentage

#printing the outcome of the county winner to the text file
winning_county_summary= (
    f"County Votes:\n"
    f"Winner:{winning_county}\n"
    f"Winning_county_vote_count:{winning_county_votes:, }"
    f"Winning_percentage: {winning_percentage: .1f}%\n"
    f"\n"
    f"---------------------------------\n"
)
#printing the output to the text file 
print(winning_county_summary)
txt.file.write(winning_county_summary)

for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
txt_file.write(winning_candidate_summary)

