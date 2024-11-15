in_input = input()
money_for_travelling = 0
sum_money_for_travelling = 0

while in_input != 'End':
    money_for_travelling = float(input())
    while money_for_travelling > sum_money_for_travelling:
        sum_money_for_travelling += float(input())
    print(f'Going to {in_input}!')
    in_input = input()
    sum_money_for_travelling = 0
