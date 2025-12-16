import numpy as np
from itertools import combinations_with_replacement

with open('input_10.txt', 'r') as in_file:
    lines = in_file.readlines()

# parse input
data = []
for line in lines:
    s = line.split(']')[0][1:].replace('.', '0').replace('#', '1')
    b = line.split('] ')[1].split(' {')[0]
    j = line.split('{')[1][:-2]
    problem = {'schematic': np.array(list(s), dtype=int),
               'buttons': [tuple(map(int, p.strip('()').split(','))) for p in b.split()],
               'joltage': np.array(j.split(','), dtype=int)}
    data.append(problem)

# translate button tuples to full-length lists
for p in data:
    p['buttons'] = [np.array([1 if i in t else 0 for i in range(len(p['schematic']))]) for t in p['buttons']]

# solve the puzzles
def solve_problem(p) -> int:
    # target state is formatted such, that any state %2 can be compared to the target
    button_presses = 1
    not_found = True
    while not_found:
        for combo in combinations_with_replacement(range(len(p['buttons'])), button_presses):
            if (np.sum([p['buttons'][i] for i in combo], axis=0) % 2 == p['schematic']).all():
                return button_presses
        button_presses += 1

total = 0
for p in data:
    total += solve_problem(p)

print(total)
