import numpy as np

def max_joltage(bank, n):
    digits = [int(b) for b in bank[:-1]]  # skip '\n'

    number = ''
    for i in range(n, 0, -1):
        if i==1:
            index = np.argmax(digits)
        else:
            index = np.argmax(digits[:-i+1])
        number += str(digits[index])

        digits = digits[index+1:]

    return int(number)

with open('input_3.txt', 'r') as in_file:
    lines = in_file.readlines()

total = 0
for bank in lines:
    total += max_joltage(bank, 12)

print(total)
