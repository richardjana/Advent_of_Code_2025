import networkx as nx
import numpy as np


### any "choke"-points along the path, that I could use to segment the problem?


with open('input_11.txt', 'r') as in_file:
    lines = in_file.readlines()

# parse input
data = {line.split(':')[0]: line[:-1].split(': ')[1].split(' ') for line in lines}

# task: find ALL paths from 'svr' to 'out' -- must visit 'dac' and 'fft'
G = nx.DiGraph()

for node in data.keys():
    G.add_node(node)

for start, ends in data.items():
    for end in ends:
        G.add_edge(start, end)

def contract_for_directed_paths(G):
    """
    Contract degree-1-in/degree-1-out nodes in a directed graph
    and remove dead-end nodes.
    Returns:
        CG : contracted directed graph
        contraction : dict mapping (u,v) -> list of nodes contracted between u and v
    """
    G = G.copy()

    changed = True
    while changed:
        changed = False

        candidates = [
            n for n in G.nodes
            if G.in_degree(n) <= 1 and G.out_degree(n) <= 1 and n not in ['svr', 'dac', 'fft', 'out']
        ]

        if not candidates:
            break

        n = candidates[0]
        (u,) = list(G.predecessors(n))
        (v,) = list(G.successors(n))

        # Avoid creating self-loops like u → u
        if u != v:
            # build direct edge
            G.add_edge(u, v)

        # remove the contracted node
        G.remove_node(n)
        changed = True

    return G


print(len(G))
G = contract_for_directed_paths(G)  # 561 -> 542
print(len(G))

# another pruning test: on the middle points 542 -> 387
for A in ['dac', 'fft']:
    reachable_from_A = nx.descendants(G, A) | {A}
    can_reach_A = nx.ancestors(G, A) | {A}
    G.remove_nodes_from([n for n in G if n not in can_reach_A and n not in reachable_from_A and n not in ['dac', 'fft']])
    print('fft' in G.nodes, 'dac' in G.nodes)
print(len(G))

'''
# detect choke points (dominators)
dom = nx.immediate_dominators(G, 'svr')
dom_tree = {v: dom[v] for v in dom if v != 'svr'}
def dominators_of(node):
    result = {node}
    while node != 'svr':
        node = dom[node]
        result.add(node)
    return result
dom_END = dominators_of('out')
mandatory_nodes = dom_END - {'svr'}
print(mandatory_nodes)  # 'dac', 'fft'
exit()
'''

for start, stop in [('svr', 'dac'), ('svr', 'fft'), ('dac', 'fft'), ('fft', 'dac'), ('dac', 'out'), ('fft', 'out')]:
    count = 0
    for path in nx.all_simple_paths(G, start, stop):
        count += 1
    print(start, stop, count)
exit()

count = 0
for path in nx.all_simple_paths(G, 'svr', 'out'):
    if 'dac' in path and 'fft' in path:
        count += 1
        print(path)

print(count)
