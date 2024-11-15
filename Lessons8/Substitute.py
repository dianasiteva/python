k = int(input())
l = int(input())
m = int(input())
n = int(input())
count = 0

for number1 in range(k, 8 + 1):
    for number2 in range(9, l - 1, -1):
        for number3 in range(m, 8 + 1):
            for number4 in range(9, n - 1, -1):
                if (number1 % 2 == 0 and not number2 % 2 == 0) and (number3 % 2 == 0 and not number4 % 2 == 0):
                    if number1 == number3 and number2 == number4:
                        print('Cannot change the same player.')
                    else:
                        print(f'{number1}{number2} - {number3}{number4}')
                    count += 1
                    if count == 6:
                        break
            if count == 6:
                break
        if count == 6:
            break
    if count == 6:
        break
