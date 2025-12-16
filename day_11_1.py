import networkx as nx

with open('input_11.txt', 'r') as in_file:
    lines = in_file.readlines()

data = {line.split(':')[0]: line[:-1].split(': ')[1].split(' ') for line in lines}

G = nx.DiGraph()
for node in data.keys():
    G.add_node(node)

for start, ends in data.items():
    for end in ends:
        G.add_edge(start, end)

all_paths = list(nx.all_simple_paths(G, 'you', 'out'))
print(len(all_paths))
