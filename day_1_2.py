with open('input_1.txt', 'r') as in_file:
    lines = in_file.readlines()

def rotate(state, value):
    if value[0] == 'L':
        sign = -1
    else:
        sign = +1
    amount = int(value[1:])

    zeros = 0
    new_state = state
    for i in range(amount):
        new_state += sign
        new_state = new_state % 100
        if new_state == 0:
            zeros += 1

    return new_state, zeros


state = 50
zero_count = 0
for line in lines:
    state, passes = rotate(state, line)

    zero_count += passes

print(zero_count)
