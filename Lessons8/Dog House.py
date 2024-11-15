x = float(input())
y = float(input())
h = float(input())

front_back_wall = x * x * 2 - 1.2 * 2
side_walls = x * y * 2 - 1.5 * 1.5 * 2
roof = x * y * 2 + x * h

red = roof / 4.3
green = (side_walls + front_back_wall) / 3.4

print(f'{green:.2f}')
print('{0:.2f}'.format(red))
