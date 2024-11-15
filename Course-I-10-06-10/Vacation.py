money_for_vacation = float(input())
start_sum = float(input())
spend_times = 0
days = 0

while spend_times < 5:
    in_text = input()
    in_sum = float(input())
    days += 1
    if in_text == 'spend':
        spend_times += 1
        if start_sum - in_sum < 0:
            start_sum = 0
        else:
            start_sum -= in_sum
    elif in_text == 'save':
        start_sum += in_sum
        spend_times = 0
    if start_sum >= money_for_vacation:
        print(f'You saved the money for {days} days.')
        break
else:
    print("You can't save the money.")
    print(f'{days}')
