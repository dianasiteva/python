PRICE_NYLON = 1.50
PRICE_PAINT = 14.50
PRICE_THINNER = 5.00
PERCENT_ADD_PAINT = 0.10
PRICE_BAGS = 0.40
ADD_NYLON = 2
PERCENT_WORKERS = 0.30

nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

sum_nylon = PRICE_NYLON * (nylon + ADD_NYLON)
sum_paint = PRICE_PAINT * (paint * (1 + PERCENT_ADD_PAINT))
sum_thinner = PRICE_THINNER * thinner
total_sum = sum_thinner + sum_paint + sum_nylon + PRICE_BAGS
sum_workers = total_sum * PERCENT_WORKERS * hours
total_price = total_sum + sum_workers

print(total_price)
