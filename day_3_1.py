import numpy as np

def max_joltage(bank):
    digits = [int(b) for b in bank[:-1]]
    i_first = np.argmax(digits[:-1])
    i_second = np.argmax(digits[i_first+1:])

    return int(bank[i_first] + bank[i_first+1+i_second])

with open('input_3.txt', 'r') as in_file:
    lines = in_file.readlines()

total = 0
for bank in lines:
    total += max_joltage(bank)

print(total)
