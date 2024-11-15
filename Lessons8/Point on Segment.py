first = int(input())
second = int(input())
point = int(input())

if first <= second:
    if first <= point <= second:
        print('in')
    else:
        print('out')
else:
    if second <= point <= first:
        print('in')
    else:
        print('out')

if abs(point - first) <= abs(point - second):
    print(abs(point - first))
else:
    print(abs(point - second))
