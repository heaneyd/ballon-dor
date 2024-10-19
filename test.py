import pandas as pd

# Sample DataFrame
data = {
    'Year': ['2012', '2012', '2013', '2012', '2014', '2012'],
    'Country': ['Burma', 'Bahamas', 'Canada', 'US Virgin Islands', 'Kyrgyzstan', 'USA'],
    'Points': [100, 200, 150, 250, 300, 350]
}

df = pd.DataFrame(data)

# Check the original DataFrame
print("Original DataFrame:")
print(df)

# Define the year and countries to remove
year_to_remove = '2012'
countries_to_remove = ['Burma', 'Bahamas', 'US Virgin Islands', 'Kyrgyzstan']

# Using .isin() to filter out the specified rows
df = df[~((df['Year'] == year_to_remove) & (df['Country'].isin(countries_to_remove)))]

# Check the updated DataFrame
print("\nUpdated DataFrame:")
print(df)

