money_per_day = float(input())
sales_money_per_day = float(input())
expenses = float(input())
gift_prise = float(input())

total_sum_days = money_per_day * 5
total_sales_money = sales_money_per_day * 5
total_sum = total_sum_days + total_sales_money
total_sum_ex = total_sum - expenses
diff = gift_prise - total_sum_ex

if gift_prise > total_sum_ex:
    print(f'Insufficient money: {diff:.2f} BGN.')
else:
    print(f'Profit: {total_sum_ex:.2f} BGN, the gift has been purchased.')
