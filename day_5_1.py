import numpy as np

with open('input_5.txt', 'r') as in_file:
    lines = in_file.readlines()

fresh_ranges = []
item_ids = []
switch = False
for line in lines:
    if line == '\n':
       switch = True
       continue

    if switch == True:
        item_ids.append(int(line[:-1]))
    else:
        fresh_ranges.append((int(line[:-1].split('-')[0]), int(line[:-1].split('-')[1])))


fresh_count = 0
for id in item_ids:
    for fr in fresh_ranges:
        if fr[0]<=id and id<=fr[1]:
            fresh_count += 1
            break

print(fresh_count)
