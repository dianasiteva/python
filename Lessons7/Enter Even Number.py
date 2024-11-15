while True:
    num = int(input('Enter even number: '))
    if num % 2 == 0:
        break
    print('The number is not even.')

print('Even number entered: %d' % num)
