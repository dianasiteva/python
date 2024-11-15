a = int(input())
b = int(input())
c = int(input())

if a + b == c:
    if a > b:
        print('%d + %d = %d' % (b, a, c))
    else:
        print('%d + %d = %d' % (a, b, c))
elif a + c == b:
    if a > c:
        print('%d + %d = %d' % (c, a, b))
    else:
        print('%d + %d = %d' % (a, c, b))
elif b + c == a:
    if b > c:
        print('%d + %d = %d' % (c, b, a))
    else:
        print('%d + %d = %d' % (b, c, a))
else:
    print('No')
