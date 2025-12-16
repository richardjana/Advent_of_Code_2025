import numpy as np

with open('input_6.txt', 'r') as in_file:
    lines = in_file.readlines()

text = []
for line in lines[:-1]:
    text.append(list(line[:-1]))

text = np.array(text)
operations = [op for op in lines[-1][:-1].split(' ') if op]

numbers = [[]]
for i_col in range(text.shape[1]):
    if np.sum(text[:, i_col] == ' ') == text.shape[0]:
        numbers.append([])
    else:
        numbers[-1].append(int(''.join(text[:, i_col])))

grand_total = 0
for op, n in zip(operations, numbers):
    if op == '+':
        grand_total += np.sum(n)
    if op == '*':
        grand_total += np.prod(n)

print(grand_total)
