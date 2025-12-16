import numpy as np

# parse input
shapes = []
sizes = []
areas = []
presents = []
input_file = open('input_12.txt_sample', 'r')
for line in input_file:
    if line in ['\n', '']:
        continue

    if len(line.split(':')[0].split('x')) == 1:  # package shape
        s = np.zeros((3, 3), dtype=int)
        for i in range(3):
            line = next(input_file)
            s[i, :] = [int(s) for s in line[:-1].replace('.', '0').replace('#', '1')]

        shapes.append(s)
        sizes.append(np.sum(s))
    else:
        x, y = line.split(':')[0].split('x')
        areas.append((int(x), int(y)))
        p = line[:-1].split(': ')[1].split(' ')
        p = [int(n) for n in p]
        presents.append(p)

# filter by size, any puzzles that cannot possibly work

print(shapes)
print(areas)
print(presents)
