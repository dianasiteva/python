in_input = input()
count = 0
min_number = 0

while in_input != 'Stop':
    if count == 0:
        min_number = int(in_input)
    else:
        if min_number > int(in_input):
            min_number = int(in_input)
    in_input = input()
    count += 1
print(f'{min_number}')
