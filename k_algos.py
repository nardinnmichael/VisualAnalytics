#!/usr/bin/env python
# coding: utf-8

# In[3]:


import networkx as nx
import matplotlib.pyplot as plt
#import json
import random

'''
with open('../VAP/train.json', 'r') as file:
    data = json.load(file)

# Create a graph of Twitter data with nodes as users and edges as communication
G = nx.Graph()
for user in data:
    user_id = user['ID']
    user_label = user['label']  # Replace 'label' with the actual label attribute name in your data
    G.add_node(user_id, label=user_label)

    
for edge in data:
    source_value = edge['ID']
    target_value = edge['ID']
    
    # Find the nodes with the specified attribute values
    source_node = next((node for node in G.nodes() if G.nodes[node]['label'] == source_value), None)
    target_node = next((node for node in G.nodes() if G.nodes[node]['label'] == target_value), None)
    
    # If both source and target nodes exist, add the edge
    if source_node and target_node:
        #and source_node != target_node:
        G.add_edge(source_node, target_node)
        # Remove self-loops from the graph
    G.remove_edges_from(nx.selfloop_edges(G))'''
# Create a random graph
G = nx.erdos_renyi_graph(50, 0.2)  # Random graph with 20 nodes and edge probability of 0.2

# Calculate node centrality
centrality = nx.betweenness_centrality(G)  # Example of betweenness centrality

# Perform k-core decomposition of the ten most central nodes
sorted_nodes = sorted(centrality, key=centrality.get, reverse=True)
top_nodes = sorted_nodes[:10]  # Select the ten most central nodes

k_core_subgraph = nx.k_core(G.subgraph(top_nodes))


# Filter nodes based on show_humans and show_bots parameters
show_humans = True  # Set to True to show human nodes
show_bots = True  # Set to True to show bot nodes

filtered_nodes = []
for node in k_core_subgraph.nodes():
    label = random.choice(['0', '1'])  # Replace this line with your random label generation logic
    if (show_humans and label == '1') or (show_bots and label == '0'):
        filtered_nodes.append(node)

filtered_subgraph = k_core_subgraph.subgraph(filtered_nodes)

# Determine if bots or humans are forming communities
bot_communities = []
human_communities = []

communities = nx.algorithms.community.greedy_modularity_communities(filtered_subgraph)

for community in communities:
    is_bot_community = all(filtered_subgraph.nodes[node].get('label') == '0' for node in community)
    is_human_community = all(filtered_subgraph.nodes[node].get('label') == '1' for node in community)

    if is_bot_community:
        bot_communities.append(community)
    elif is_human_community:
        human_communities.append(community)

# Plot the original graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=200)
plt.title("Random Graph")
plt.show()

# Plot the filtered k-core subgraph
nx.draw(filtered_subgraph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=200)
plt.title("Filtered K-Core Subgraph")
plt.show()

# Print the centrality values
print("Node Centrality:")
for node, centrality_value in centrality.items():
    print(f"Node {node}: {centrality_value}")


# Print the communities
print("Detected Communities:")
for i, community in enumerate(communities):
    print(f"Community {i+1}: {community}")


# In[ ]:




