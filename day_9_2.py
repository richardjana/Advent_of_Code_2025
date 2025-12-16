import numpy as np

with open('input_9.txt', 'r') as in_file:
    lines = in_file.readlines()

red_tiles = []
for line in lines:
    red_tiles.append(tuple(map(int, line.strip().split(','))))

green_tiles = []
# around the loop
for t1, t2 in zip (red_tiles, red_tiles[1:]+[red_tiles[0]]):
    if t1[0] == t2[0]:
        for i in range(min(t1[1], t2[1])+1, max(t1[1], t2[1])):
            green_tiles.append((t1[0], i))
    else:
        for i in range(min(t1[0], t2[0])+1, max(t1[0], t2[0])):
            green_tiles.append((i, t1[1]))
#print(red_tiles)
#print(green_tiles)

# inner tiles: row-wise start from left, count the crossings
columns = list(zip(*red_tiles))
bounds = [(min(col), max(col)) for col in columns]
for i in range(bounds[0][0], bounds[0][1]+1):
    count = 0
    is_wall = False
    for j in range(bounds[1][0], bounds[1][1]+1):
        if (i, j) in red_tiles:  # corner
            if is_wall:
                count = 1
            is_wall = ~is_wall
        elif (i, j) in green_tiles: # no corners
            count += 1
        elif count % 2 == 1:
            green_tiles.append((i, j))
'''
p = np.zeros((15,15), dtype=int)
for tile in red_tiles:
    p[tile[0], tile[1]] = 1
for tile in green_tiles:
    p[tile[0], tile[1]] = 2
print(p)
'''
areas = np.zeros((len(red_tiles), len(red_tiles)), dtype=int)
for i in range(len(red_tiles)):
    for j in range(i+1, len(red_tiles)):
        areas[i, j] = (abs(red_tiles[i][0]-red_tiles[j][0])+1) * (abs(red_tiles[i][1]-red_tiles[j][1])+1)

# check if contains any forbidden tiles
def check_allowed_tiles(t1, t2):
    for i in range(min(t1[0], t2[0]), max(t1[0], t2[0])+1):
        for j in range(min(t1[1], t2[1]), max(t1[1], t2[1])+1):
            if (i, j) not in red_tiles + green_tiles:
                print(i, j)
                return False
    return True

allowed = False
while not allowed:
    i, j = np.unravel_index(np.argmax(areas), areas.shape)
    print(red_tiles[i], red_tiles[j], areas[i, j])
    if check_allowed_tiles(red_tiles[i], red_tiles[j]):
        allowed = True
    else:
        areas[i, j] = 0

print(areas[i, j])
