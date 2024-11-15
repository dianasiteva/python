x = int(input())
y = int(input())

# fugure 1 f1
f1_x1 = 4
f1_x2 = 10
f1_y1 = -5
f1_y2 = 3
#figure 2 f2
f2_x1 = 2
f2_x2 = 12
f2_y1 = -3
f2_y2 = 1

if f1_x1 <= x <= f1_x2 and f1_y1 <= y <= f1_y2 or f2_x1 <= x <= f2_x2 and f2_y1 <= y <= f2_y2:
    print('in')
else:
    print('out')
