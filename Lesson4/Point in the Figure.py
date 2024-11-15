h = int(input())
x = int(input())
y = int(input())

outrec1 = x < 0 or x > (3 * h) or y < 0 or y > h
outrec2 = x < h or x > (2 * h) or y < 0 or y > (4 * h)
in_rec1 = 0 < x < (3 * h) and 0 < y < h
in_rec2 = h < x < (2 * h) and 0 < y < (4 * h)

if outrec1 and outrec2:
    print('outside')
elif in_rec1 or in_rec2:
    print('inside')
else:
    print('border')