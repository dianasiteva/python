import math

n = int(input())

roof_rows = 0
room_rows = 0
dach_nums = 0

if n % 2 == 0:
    roof_rows = math.floor(n / 2) - 1
    room_rows = roof_rows + 1
    for i in range(1, roof_rows + 1):
        dach_nums = math.floor(n / 2) - i
        print('-' * dach_nums + '**' * i + '-' * dach_nums)
    print('*' * n)
    for i in range(0, room_rows):
        print('|' + '*' * (n - 2) + '|')
else:
    roof_rows = math.floor(n / 2)
    room_rows = roof_rows
    for i in range(0, roof_rows):
        dach_nums = math.floor((n - 1 - 2 * i) / 2)
        print('-' * dach_nums + '*' * (n - 2 * dach_nums)  + '-' * dach_nums)
    print('*' * n)
    for i in range(0, room_rows):
        print('|' + '*' * (n - 2) + '|')
