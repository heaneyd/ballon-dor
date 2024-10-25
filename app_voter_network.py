import pandas as pd
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset
@st.cache_data
def load_data():
    file_path = 'outfile.dat'
    data = pd.read_csv(file_path, delimiter='|', header=None)
    data.columns = ['Year', 'Country', 'Continent', 'Ranking Date', 'Rank', 'Award name', 'Voter Name', 'Voter Role', 'Player', 'Player National Team', 'Player Continent', 'Player Club Team', 'Position', 'Points']
    return data

data = load_data()

# Filter data for 2023 Ballon D'Or
filtered_data = data[(data['Year'] == 2023) & (data['Award name'] == "Ballon D'Or")]

# Initialize the graph
G = nx.Graph()

# Add nodes and edges
for _, row in filtered_data.iterrows():
    voter = row['Voter Name']
    player = row['Player']
    points = row['Points']

    # Add nodes for voters and players
    G.add_node(voter, type='voter')
    G.add_node(player, type='player')

    # Add edge with weight based on points awarded
    G.add_edge(voter, player, weight=points)

# Draw the network
st.write("### Ballon D'Or Voting Network - 2023")
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, seed=42)  # Use spring layout for better spacing
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700, alpha=0.8)
nx.draw_networkx_edges(G, pos, width=1, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=10)

# Edge weights for better visualization
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

st.pyplot(plt)


# (Add nodes and edges for G based on your data)
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

# Create a DataFrame with centrality measures
centrality_df = pd.DataFrame({
    "Node": list(degree_centrality.keys()),
    "Degree Centrality": list(degree_centrality.values()),
    "Betweenness Centrality": list(betweenness_centrality.values())
})

# Sort by Degree Centrality in descending order
centrality_df = centrality_df.sort_values(by="Degree Centrality", ascending=False)

# Apply conditional formatting in Streamlit
st.write("### Centrality Measures")
st.dataframe(centrality_df.style
    .background_gradient(cmap="YlGn", subset=["Degree Centrality"])
    .background_gradient(cmap="Blues", subset=["Betweenness Centrality"])
    .format({"Degree Centrality": "{:.2f}", "Betweenness Centrality": "{:.2f}"}))


# Calculate centrality
st.write("### Network Analysis")
#degree_centrality = nx.degree_centrality(G)
#betweenness_centrality = nx.betweenness_centrality(G)
st.write("Degree Centrality:", degree_centrality)
st.write("Betweenness Centrality:", betweenness_centrality)
