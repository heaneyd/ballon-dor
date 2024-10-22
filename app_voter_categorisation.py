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
vote_matrix = filtered_data.pivot_table(index='Voter Name', columns='Player', values='Points', fill_value=0)
#vote_matrix_aggregated = vote_matrix.reshape((len(vote_matrix) // 5, 5)).mean(axis=1)

# Perform KMeans clustering
num_clusters = st.sidebar.slider("Number of Clusters", min_value=2, max_value=10, value=3)
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
vote_matrix['Cluster'] = kmeans.fit_predict(vote_matrix)

# Display the clusters
st.write("### Journalist Clusters")
#st.write(filtered_data[['Voter Name', 'cluster']])
st.write(vote_matrix)

# Show a heatmap for the clustering
plt.figure(figsize=(10, 25))
sns.heatmap(vote_matrix.sort_values(by='Cluster', ascending=True), cmap="coolwarm", cbar_kws={'label': 'Points'})
plt.title("Journalist Voting Patterns Heatmap")
st.pyplot(plt)
