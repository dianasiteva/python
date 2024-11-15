type = input().lower()
rows = int(input())
columns = int(input())

price = 0
br = rows * columns

if type == 'premiere':
    price = 12
elif type == 'normal':
    price = 7.5
elif type == 'discount':
    price = 5

if price > 0:
    print('%.2f' % (price * br))
else:
    print('error')

