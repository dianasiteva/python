age = int(input())
price_w_m = float(input())
toy_price = int(input())
sum_lv = 0
toys = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        sum_lv += i / 2 * 10 - 1
    else:
        toys += 1

sum_lv += toy_price * toys

if price_w_m > sum_lv:
    print(f'No! {(price_w_m - sum_lv):.2f}')
else:
    print(f'Yes! {(sum_lv - price_w_m):.2f}')
