import numpy as np

with open('input_9.txt', 'r') as in_file:
    lines = in_file.readlines()

tiles = []
for line in lines:
    tiles.append(tuple(map(int, line.strip().split(','))))

areas = np.zeros((len(tiles), len(tiles)), dtype=int)
for i in range(len(tiles)):
    for j in range(i+1, len(tiles)):
        areas[i, j] = (abs(tiles[i][0]-tiles[j][0])+1) * (abs(tiles[i][1]-tiles[j][1])+1)

print(np.max(areas))
