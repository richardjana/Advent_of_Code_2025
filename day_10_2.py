import numpy as np
import pulp

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
    n = len(p['joltage'])
    m = len(p['buttons'])

    B = np.stack(p['buttons'], axis=1)

    prob = pulp.LpProblem('LinearCombination', pulp.LpMinimize)

    coeffs = [pulp.LpVariable(f"c{i}", lowBound=0, cat='Integer') for i in range(m)]

    prob += pulp.lpSum(coeffs)

    for row in range(n):
        prob += pulp.lpSum(B[row, col] * coeffs[col] for col in range(m)) == p['joltage'][row]
    prob.solve()

    return np.sum([pulp.value(c) for c in coeffs])


total = 0
for i, p in enumerate(data):
    pushes = solve_problem(p)
    print(i, pushes)
    total += pushes

print(total)
