line = input().lower()
sum = 0
l1 = '('
l2 = ' = '
n = 0

for c in line:
    if c == 'a':
        sum += 1
        n += 1
        if l1 == '(':
            l1 += 'a'
            l2 += '1'
        else:
            l1 += '+a'
            l2 += '+1'

    elif c == 'e':
        sum += 2
        n += 1
        if l1 == '(':
            l1 += 'e'
            l2 += '2'
        else:
            l1 += '+e'
            l2 += '+2'

    elif c == 'i':
        sum += 3
        n += 1
        if l1 == '(':
            l1 += 'i'
            l2 += '3'
        else:
            l1 += '+i'
            l2 += '+3'

    elif c =='o':
        sum += 4
        n += 1
        if l1 == '(':
            l1 += 'o'
            l2 += '4'
        else:
            l1 += '+o'
            l2 += '+4'

    elif c == 'u':
        sum += 5
        n += 1
        if l1 == '(':
            l1 += 'u'
            l2 += '5'
        else:
            l1 += '+u'
            l2 += '+5'

print(sum)
if n > 1:
    print(l1 + l2 + ' = ' + str(sum) + ')')
else:
    print(l1 + l2 + ')')
