def is_invalid(id):
    s = str(id)

    for n in range(2, len(s)+1):
        if len(s) % n != 0:
            continue

        l = len(s)//n
        parts = [s[i*l:(i+1)*l] for i in range(n)]

        if len(set(parts)) == 1:
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
