x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x = float(input())
y = float(input())

on_left_side = x == x1 and y1 <= y <= y2
on_right_side = x == x2 and y1 <= y <= y2
on_up_side = y == y1 and x1 <= x <= x2
on_down_side = y == y2 and x1 <= x <= x2

if on_down_side or on_up_side or on_right_side or on_left_side:
    print('Border')
else:
    print('Inside / Outside')
