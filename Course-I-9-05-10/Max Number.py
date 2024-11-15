in_input = input()
count = 0
max_number = 0

while in_input != 'Stop':
    if count == 0:
        max_number = int(in_input)
    else:
        if max_number < int(in_input):
            max_number = int(in_input)
    in_input = input()
    count += 1
print(f'{max_number}')
