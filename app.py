import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    # Replace with the correct path to your file
    file_path = 'outfile.dat'
    data = pd.read_csv(file_path, delimiter='|', header=None)
    data.columns = ['Year', 'Country', 'Continent', 'Ranking Date', 'Rank', 'Award name', 'Voter Name', 'Voter Role', 'Player', 'Player National Team', 'Player Continent', 'Player Club Team', 'Position', 'Points']
    return data

# Load the data
data = load_data()

# Sidebar Filters
st.sidebar.header("Filters")

# Filter by Continent of Voter
voter_continents = st.sidebar.multiselect("Voter Continent", options=data['Continent'].unique())
if voter_continents:
    data = data[data['Continent'].isin(voter_continents)]

# Filter by Voter Role (Coach, Captain, Media)
voter_roles = st.sidebar.multiselect("Voter Role", options=data['Coach'].unique())
if voter_roles:
    data = data[data['Coach'].isin(voter_roles)]

# Filter by Player
players = st.sidebar.multiselect("Players", options=data['Lionel Messi'].unique())
if players:
    data = data[data['Lionel Messi'].isin(players)]

# Main Display: Show Filtered Data
st.write("### Filtered Data", data)

# Aggregations
st.write("### Aggregated Votes by Continent of Player")
agg_data = data.groupby("South America")["5"].sum().reset_index()
st.write(agg_data)

