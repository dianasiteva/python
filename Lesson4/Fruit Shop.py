fruit = input().lower()
day = input().lower()
quantity = float(input())

price = 0
err = 0

if day == 'saturday' or day == 'sunday':
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3
    elif fruit == 'pineapple':
        price = 5.6
    elif fruit == 'grapes':
        price = 4.2
elif day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday':
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.2
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.7
    elif fruit == 'pineapple':
        price = 5.5
    elif fruit == 'grapes':
        price = 3.85
else:
    #print('error')
    err = 1

if price != 0:
    print('%.2f' % (price * quantity))
else:
    print('error')