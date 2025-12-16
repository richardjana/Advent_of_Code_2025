def is_invalid(id):
    s = str(id)

    if s[:len(s)//2] == s[len(s)//2:]:
        return True

    return False

with open('input_2.txt', 'r') as in_file:
    line = in_file.readlines()

id_ranges = line[0].split(',')
ids = [(int(range.split('-')[0]), int(range.split('-')[1])) for range in id_ranges]


invalid_sum = 0
for start, stop in ids:
    for i in range(start, stop+1):
        if is_invalid(i):
            invalid_sum += i

print(invalid_sum)
