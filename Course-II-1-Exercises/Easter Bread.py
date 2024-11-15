budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
total_sum = 0
colored_eggs = 0
for_one_bread = flour_price + eggs_price + milk_price
number_of_loaves = 0

while budget >= total_sum + for_one_bread:
    number_of_loaves += 1
    colored_eggs += 3
    total_sum += for_one_bread
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)
else:
    money_left = budget - total_sum
    print(f'You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')
