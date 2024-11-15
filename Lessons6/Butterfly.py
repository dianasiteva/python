n = int(input())

part_row_odd = '*' * (n - 2)
part_row_even = '-' * (n - 2)

for i in range(1, (n - 2) + 1):
    if i % 2 == 0:
        print('{0}\\ /{0}'.format(part_row_even))
    else:
        print('{0}\\ /{0}'.format(part_row_odd))

print(' ' * (n - 1) + '@')

for i in range(1, (n - 2) + 1):
    if i % 2 == 0:
        print('{0}/ \\{0}'.format(part_row_even))
    else:
        print('{0}/ \\{0}'.format(part_row_odd))
