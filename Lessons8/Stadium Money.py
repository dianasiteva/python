sektors = int(input())
capacity = int(input())
ticket_price = float(input())

all_sum = capacity * ticket_price
single_sektor_profit = all_sum / sektors
charity = (all_sum - single_sektor_profit * 0.75) / 8

print(f'Total income - {all_sum:.2f} BGN')
print(f'Money for charity - {charity:.2f} BGN')
