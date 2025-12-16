import numpy as np

with open('input_6.txt', 'r') as in_file:
    lines = in_file.readlines()

numbers = []
for line in lines[:-1]:
    numbers.append([int(n) for n in line[:-1].split(' ') if n])
numbers = np.array(numbers)

operations = [op for op in lines[-1][:-1].split(' ') if op]
results = []

for i, op in enumerate(operations):
    if op == '+':
        results.append(np.sum(numbers[:, i]))
    if op == '*':
        results.append(np.prod(numbers[:, i]))

print(results)
print(np.sum(results))
