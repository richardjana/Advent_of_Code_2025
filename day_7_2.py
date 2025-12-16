import numpy as np

with open('input_7.txt', 'r') as in_file:
    lines = in_file.readlines()

grid = []
for line in lines:
    grid.append(list(line[:-1]))
grid = np.array(grid)

time_lines = np.zeros(grid.shape, dtype=int)
time_lines[0, 70] = 1

for i in range(1, grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i, j] == '.':
            time_lines[i, j] += time_lines[i-1, j]
        else:
            time_lines[i, j-1] += time_lines[i-1, j]
            time_lines[i, j+1] += time_lines[i-1, j]

print(np.sum(time_lines[-1, :]))
