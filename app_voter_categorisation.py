import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
@st.cache_data
def load_data():
    file_path = 'outfile.dat'
    data = pd.read_csv(file_path, delimiter='|', header=None)
    data.columns = ['Year', 'Country', 'Continent', 'Ranking Date', 'Rank', 'Award name', 'Voter Name', 'Voter Role', 'Player', 'Player National Team', 'Player Continent', 'Player Club Team', 'Position', 'Points']
    return data

# Load the data
data = load_data()

# Filter for 2023 Ballon D'Or
filtered_data = data[(data['Year'] == 2023) & (data['Award name'] == "Ballon D'Or")]

# Create a matrix where rows are journalists (Voter Name) and columns are players
# 1. Calculate the total points per player
total_points_per_player = filtered_data.groupby("Player")["Points"].sum().sort_values(ascending=False)

# 2. Get the sorted order of players by total points
sorted_players = total_points_per_player.index.tolist()
vote_matrix = filtered_data.pivot_table(index='Country', columns='Player', values='Points', fill_value=0)
vote_matrix = vote_matrix[sorted_players]

#vote_matrix_aggregated = vote_matrix.reshape((len(vote_matrix) // 5, 5)).mean(axis=1)

# Perform KMeans clustering
num_clusters = st.sidebar.slider("Number of Clusters", min_value=2, max_value=10, value=3)
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
vote_matrix['Cluster'] = kmeans.fit_predict(vote_matrix)

# Display the clusters
st.write("### Country Clusters")
#st.write(filtered_data[['Voter Name', 'cluster']])
st.write(vote_matrix)

# Show a heatmap for the clustering
# Sort voters by their cluster labels
sorted_vote_matrix = vote_matrix.sort_values(by='Cluster', ascending=True)

plt.figure(figsize=(10, 24))
ax = sns.heatmap(sorted_vote_matrix.drop(columns=['Cluster']), cmap="coolwarm", cbar_kws={'label': 'Points'})


plt.title("Country Voting Patterns Heatmap")
st.pyplot(plt)
