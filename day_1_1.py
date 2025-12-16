with open('input_1.txt', 'r') as in_file:
    lines = in_file.readlines()

state = 50
zero_count = 0
for line in lines:
    rotation = int(line[1:])
    if line[0] == 'L':
        state -= rotation
    else:
        state += rotation

    state = state % 100

    if state == 0:
        zero_count += 1

print(zero_count)
