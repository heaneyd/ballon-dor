import pandas as pd

# Let me load and inspect the contents of the file to understand its structure and data.
file_path = 'outfile.dat'

# Read the file and display its contents
with open(file_path, 'r') as file:
    file_content = file.read()



# Split the file content into a list of lines and then into columns for further analysis
data_lines = file_content.strip().split("\n")
columns = [
    "Year", "Country", "Continent", "Date", "Ranking", "Award Type", "Voter", "Voter Role",
    "Player", "Player Nationality", "Player Continent", "Club", "Position", "Points"
]

# Create a DataFrame from the data
data = [line.split("|") for line in data_lines]
df = pd.DataFrame(data, columns=columns)

# Let's first calculate the global distribution (fair vote) for players from each continent
player_continent_distribution = df['Player Continent'].value_counts(normalize=True).reset_index()
player_continent_distribution.columns = ['Continent', 'Fair Vote Percentage']
player_continent_distribution['Fair Vote Percentage'] = player_continent_distribution['Fair Vote Percentage'] * 100

# Now calculate the actual voting behavior of each continent (how much they vote for players from different continents)
voting_patterns = df.groupby(['Continent', 'Player Continent']).size().unstack(fill_value=0)

# Normalize the voting patterns by continent to get percentages
voting_patterns_percent = voting_patterns.div(voting_patterns.sum(axis=1), axis=0) * 100

# Merge the fair vote percentages with the actual voting percentages
bias_analysis = voting_patterns_percent.copy()
for continent in bias_analysis.columns:
    bias_analysis[continent] = bias_analysis[continent] - player_continent_distribution.set_index('Continent').loc[continent, 'Fair Vote Percentage']

bias_analysis.reset_index()

print(player_continent_distribution)
print(bias_analysis) 
