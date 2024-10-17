import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    # Replace with the correct path to your file
    file_path = 'outfile.dat'
    data = pd.read_csv(file_path, delimiter='|', header=None)
    data.columns = ['Year', 'Country', 'Continent', 'Ranking Date', 'Rank', 'Award name', 'Voter Name', 'Voter Role', 'Player', 'Player National Team', 'Player Continent', 'Player Club Team', 'Position', 'Points']
    data['Top 100'] = data['Rank'].apply(lambda x: 'Yes' if x <= 100 else 'No')
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
top100 = st.sidebar.multiselect("Top 100", options=data['Top 100'].unique())
if top100:
    data = data[data['Top 100'].isin(top100)]

# Filter by Player
voter_role = st.sidebar.multiselect("Voter Role", options=data['Voter Role'].unique())
if voter_role:
    data = data[data['Voter Role'].isin(voter_role)]

# Main Display: Show Filtered Data
st.write("### Filtered Data", data)

# Aggregations
st.write("### Aggregated Votes by Player")
agg_data = data.groupby(["Player","Voter Role"])["Points"].sum().reset_index()
total_by_role = agg_data.groupby("Voter Role")["Points"].sum()
agg_data['total'] = agg_data['Voter Role'].map(total_by_role)
agg_data['percent'] = (agg_data['Points']/agg_data['total']) * 100

#finally get the avg of percent and sum of points

pts = agg_data.groupby(["Player"])["Points"].sum()
avg = agg_data.groupby(["Player"])["percent"].mean()

display_df = pd.DataFrame({'Total Points': pts, 'Avg Percent': avg*100}).reset_index()
st.write(display_df.sort_values(by='Total Points', ascending=False))
