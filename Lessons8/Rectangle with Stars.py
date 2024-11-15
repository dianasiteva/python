import math

n = int(input())
rows = n

if n % 2 == 0:
    rows -= 1

print('%' * 2 * n)

for i in range(0, rows):
    print('%', end='')

    if i == math.floor((rows / 2)):
        print(" " * (n - 2) + '**' + ' ' * (n - 2), end='')
    else:
        print(' ' * (n * 2 - 2), end='')

    print('%')

print('%' * 2 * n)
