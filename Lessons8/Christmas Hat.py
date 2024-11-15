n = int(input())
rows = 2 * n + 5
columns = 4 * n + 1

number = int((columns - 3) / 2)

print('.' * number + '/|\\' + '.' * number )
print('.' * number + '\\|/' + '.' * number )

for i in range(0, n * 2):
    number = int((columns - 3) / 2 - i)
    print('.' * number + '*' + '-' * i + '*' + '-' * i + '*' + '.' * number)

print('*' * columns)
print('*.' * 2 * n + '*')
print('*' * columns)
