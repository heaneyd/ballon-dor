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
award_name = st.sidebar.multiselect("Award", options=data['Award name'].unique())
if award_name:
    data = data[data['Award name'].isin(award_name)]

# Filter by Voter Role (Coach, Captain, Media)
year = st.sidebar.multiselect("Year", options=data['Year'].unique())
if year:
    data = data[data['Year'].isin(year)]

# Filter by Player
rank = st.sidebar.multiselect("Rank", options=data['Rank'].unique())
if rank:
    data = data[data['rank'].isin(rank)]

# Main Display: Show Filtered Data
st.write("### Filtered Data", data)

# Aggregations
st.write("### Aggregated Votes by Continent of Player")
agg_data = data.groupby("Player")["Points"].sum().reset_index()
st.write(agg_data)

