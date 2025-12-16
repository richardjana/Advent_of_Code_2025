import networkx as nx
import numpy as np

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
    Contract degree-1-in/degree-1-out nodes in a directed graph and remove dead-end nodes.
    """
    G = G.copy()

    changed = True
    while changed:
        changed = False

        candidates = [n for n in G.nodes
                      if G.in_degree(n) <= 1 and G.out_degree(n) <= 1 and n not in ['svr', 'dac', 'fft', 'out']]

        if not candidates:
            break

        n = candidates[0]
        (u,) = list(G.predecessors(n))
        (v,) = list(G.successors(n))

        if u != v:  # build direct edge
            G.add_edge(u, v)

        G.remove_node(n)  # remove the contracted node
        changed = True

    return G


G = contract_for_directed_paths(G)  # 561 -> 542

for A in ['dac', 'fft']:  # pruning on the middle points 542 -> 387
    reachable_from_A = nx.descendants(G, A) | {A}
    can_reach_A = nx.ancestors(G, A) | {A}
    G.remove_nodes_from([n for n in G
                         if n not in can_reach_A
                         and n not in reachable_from_A
                         and n not in ['dac', 'fft']])
    print('fft' in G.nodes, 'dac' in G.nodes)
print(len(G))

def count_paths(G, start, end):
    """ dynamic programming on DAG """
    order = list(nx.topological_sort(G))
    ways = {n: 0 for n in G}
    ways[start] = 1

    for u in order:
        for v in G.successors(u):
            ways[v] += ways[u]

    return ways[end]

print(count_paths(G, 'svr', 'dac')*count_paths(G, 'dac', 'fft')*count_paths(G, 'fft', 'out') +
      count_paths(G, 'svr', 'fft')*count_paths(G, 'fft', 'dac')*count_paths(G, 'dac', 'out'))
