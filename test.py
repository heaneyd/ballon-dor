# Input dictionaries
totals = {'Europe': 100, 'South America': 50}
distribution = {'Europe': 0.7, 'South America': 0.2, 'Asia': 0.1}

# Output dictionary to store the results
output = {}

# Iterate over each continent in the totals
for continent, total_voters in totals.items():
    # For each continent, calculate the distribution based on the percentages
    output[continent] = {target_continent: total_voters * percent for target_continent, percent in distribution.items()}

# Display the output
print(output)

