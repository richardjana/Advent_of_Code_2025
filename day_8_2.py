import numpy as np

with open('input_8.txt', 'r') as in_file:
    lines = in_file.readlines()

jbs = []
for line in lines:
    jbs.append(tuple(map(int, line.strip().split(','))))

distances = np.zeros((len(jbs), len(jbs))) + np.inf
for i in range(len(jbs)):
    for j in range(i+1, len(jbs)):
        distances[i, j] = np.linalg.norm(np.array(jbs[i])-np.array(jbs[j]))

circuits = [[i] for i in range(len(jbs))]

while len(circuits) > 1:
    # find closest pair of boxes (not directly connected)
    mi, mj = np.unravel_index(np.argmin(distances), distances.shape)
    distances[mi, mj] = np.inf

    # find circuits
    for c in range(len(circuits)):
        if mi in circuits[c]:
            c0 = c
        if mj in circuits[c]:
            c1 = c

    # update circuits
    if c0 == c1:
        continue
    else:  # merge
        circuits.append(circuits[c0]+circuits[c1])
        for k in sorted([c0, c1], reverse=True):
            del circuits[k]

print(jbs[mi][0] * jbs[mj][0])
