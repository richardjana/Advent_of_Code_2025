import numpy as np

def count_accessible_rolls(g):
    n_neighbors = np.zeros(g.shape)

    for shift in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        n_neighbors += np.roll(g, shift, axis=(0, 1))

    return g.copy() * ((n_neighbors < 4)-1)*(-1)


with open('input_4.txt', 'r') as in_file:
    lines = in_file.readlines()

grid_str = [list(line[:-1].replace('.', '0').replace('@', '1')) for line in lines]
grid_orig = np.pad(np.array(grid_str, dtype=np.int32), 1)

grid_old = grid_orig.copy()
grid_new = count_accessible_rolls(grid_old)
while np.sum(grid_new) < np.sum(grid_old):
    grid_old = grid_new
    grid_new = count_accessible_rolls(grid_old)

print(np.sum(grid_orig) -np.sum(grid_new))
