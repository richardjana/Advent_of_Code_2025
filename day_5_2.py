import numpy as np

with open('input_5.txt', 'r') as in_file:
    lines = in_file.readlines()

fresh_ranges = []
for line in lines:
    if line == '\n':
       break

    fresh_ranges.append((int(line[:-1].split('-')[0]), int(line[:-1].split('-')[1])))

fresh_ranges = sorted(fresh_ranges)

# try combining ranges
def try_replacing(fr):
    for i in range(len(fr)):
        for j in range(i+1, len(fr)):
            if fr[i][1] >= fr[j][0]:  # overlapping; works because sorted
                fr.append((fr[i][0], max(fr[i][1], fr[j][1])))  # second one might be completely in the first one
                del fr[j]  # delete only these 2
                del fr[i]
                return True, sorted(fr)

    return False, fr


success = True
while success:
    success, fresh_ranges = try_replacing(fresh_ranges)

fr_lengths = [fr[1]-fr[0]+1 for fr in fresh_ranges]
print(np.sum(fr_lengths))
