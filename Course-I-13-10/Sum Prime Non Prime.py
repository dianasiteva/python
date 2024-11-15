in_input = input()
sum_prime = 0
sum_no_prime = 0

while in_input != 'stop':
    number = int(in_input)
    flag = True
    if number < 0:
        print('Number is negative.')
    elif number == 1:
        sum_prime += 1
    elif number > 1:
        for i in range(2, number):
            if number % i == 0:
                sum_no_prime += number
                flag = False
                break
        if flag:
            sum_prime += number
    in_input = input()
else:
    print(f'Sum of all prime numbers is: {sum_prime}')
    print(f'Sum of all non prime numbers is: {sum_no_prime}')
