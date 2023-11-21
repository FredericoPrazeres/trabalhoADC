import pandas as pd

# Read the 'paths_finished.tsv' file
paths = pd.read_csv('tsvs/paths_finished.tsv', sep='\t', header=None)

# Get the paths from the 4th column and split them by semicolons
all_paths = paths.iloc[:, 3].str.split(';')

# Create sets to store unique start and end nodes
unique_start_nodes = set()
unique_end_nodes = set()

# Extract start and end nodes from each path
for path in all_paths:
    # Exclude backspace nodes ('<') from the path
    path = [node for node in path if node != '<']
    if len(path) > 1:  # Exclude single-node paths
        unique_start_nodes.add(path[0])  # First node is the start node
        unique_end_nodes.add(path[-1])   # Last node is the end node

# Convert sets to lists and sort them
unique_start_nodes = sorted(list(unique_start_nodes))
unique_end_nodes = sorted(list(unique_end_nodes))

# Display the unique start and end nodes in tuples
start_end_tuples = list(zip(unique_start_nodes, unique_end_nodes))

print("Start and End Node Tuples:")
for pair in start_end_tuples:
    print(pair)