import pandas as pd
import networkx as nx

# Load Links data from TSV file
df_links = pd.read_csv('links.tsv')

# Create graph
g_links = nx.from_pandas_edgelist(df_links, source=0, target=1)

# Calculate shortest path length for each pair of nodes
shortest_paths = dict(nx.all_pairs_shortest_path_length(g_links))

# Calculate diameter of the graph
try:
    diameter = nx.diameter(g_links)
except nx.NetworkXError:
    diameter = "Graph is not connected."

print("Shortest Paths:", shortest_paths)
print("Diameter:", diameter)

# Load Categoriesdata from TSV file
df_categories = pd.read_csv('categories.tsv')

# Create graph
g_categories = nx.from_pandas_edgelist(df_categories, source=0, target=1)

# Calculate shortest path length for each pair of nodes
shortest_paths = dict(nx.all_pairs_shortest_path_length(df_categories))

# Calculate diameter of the graph
try:
    diameter = nx.diameter(g_categories)
except nx.NetworkXError:
    diameter = "Graph is not connected."

print("Shortest Paths:", shortest_paths)
print("Diameter:", diameter)