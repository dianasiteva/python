number_of_orders = int(input())
total_sum = 0
order_sum = 0

for i in range(0, number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    number_of_capsules = int(input())
    if days < 1 or days > 31:
        continue
    elif number_of_capsules > 2000 or number_of_capsules < 1:
        continue
    elif price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    order_sum = days * price_per_capsule * number_of_capsules
    total_sum += order_sum
    print(f'The price for the coffee is: ${order_sum:.2f}')

print(f'Total: ${total_sum:.2f}')
