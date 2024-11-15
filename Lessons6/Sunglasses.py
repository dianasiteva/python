n = int(input())

long_row = '*{0}*{1}*{2}*' .format('/' * (2 * n - 2), '|' * n, '/' * (2 * n - 2))
short_row = '*{0}*{1}*{2}*' .format('/' * (2 * n - 2), ' ' * n, '/' * (2 * n - 2))
short_row_number_up = 0
short_row_number_down = 0

short_row_number = (n - 3)

if short_row_number % 2 == 0:
    short_row_number_up = int(short_row_number / 2)
    short_row_number_down = short_row_number_up
else:
    short_row_number_up = int((short_row_number) / 2)
    short_row_number_down = short_row_number_up + 1

if short_row_number == 0:
    print('*' * 2 * n + ' ' * n + '*' * 2 * n)
    print(long_row)
    print('*' * 2 * n + ' ' * n + '*' * 2 * n)
else:
    print('*' * 2 * n + ' ' * n + '*' * 2 * n)
    for i in range(0, short_row_number_up):
        print(short_row)
    print(long_row)
    for i in range(0, short_row_number_down):
        print(short_row)
    print('*' * 2 * n + ' ' * n + '*' * 2 * n)
