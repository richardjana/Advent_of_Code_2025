import numpy as np

with open('input_7.txt', 'r') as in_file:
    lines = in_file.readlines()

grid = []
for line in lines:
    grid.append(list(line[:-1]))
grid = np.array(grid)

beams = np.argwhere(grid[0] == 'S').tolist()
splits = 0
for i in range(1, grid.shape[0]):
    new_beams = []
    for b in beams[-1]:
        match grid[i, b]:
            case '.':
                new_beams.append(b)
            case '^':
                splits += 1
                new_beams.append(b-1)
                new_beams.append(b+1)

    beams.append(list(set(new_beams)))

print(splits)
