age_of_Lilliy = int(input())
w_mashine_price = float(input())
toy_price = int(input())
toy_number = 0
total_sum = 0
money_number = 0

if age_of_Lilliy % 2 == 0:
    toy_number = age_of_Lilliy / 2
    money_number = toy_number
else:
    toy_number = (age_of_Lilliy + 1) / 2
    money_number = toy_number - 1

for i in range(0, int(money_number)):
    total_sum += (i + 1) * 10 - 1

total_sum += toy_number * toy_price
if total_sum >= w_mashine_price:
    print('Yes! %.2f' % (total_sum - w_mashine_price))
else:
    print('No! %.2f' % (w_mashine_price - total_sum))
