n = int(input())

outer_dots = int((n - 1) / 2)
inner_dots = n - 2

print('{0}{1}{0}'.format('.' * outer_dots, '#' * n))

for i in range(n - 2):
    print('{0}#{1}#{0}'.format('.' * outer_dots, '.' * inner_dots))

print('{0}#{1}#{0}'.format('#' * outer_dots, '.' * inner_dots))

outer_dots = 1
inner_dots = 2 * n - 5

for i in range(n - 2):
    print('{0}#{1}#{0}'.format('.' * outer_dots, '.' * inner_dots))
    outer_dots += 1
    inner_dots -= 2

print('{0}#{0}'.format('.' * (n - 1)))
