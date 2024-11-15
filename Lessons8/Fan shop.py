budget = int(input())
n = int(input())
total_amount = 0

for item in range(0, n):
    input_item = input().lower()
    if input_item == 'boodie':
        total_amount += 30
    elif 'keychain' == input_item:
        total_amount += 4
    elif 't-shirt' == input_item:
        total_amount += 20
    elif 'flag' == input_item:
        total_amount += 15
    elif 'sticker' == input_item:
        total_amount += 1

diff = abs(budget - total_amount)
if budget >= total_amount:
    print(f'You bought {n} items and left with {diff} lv.')
else:
    print(f'Not enough money, you need {diff} more lv.')
