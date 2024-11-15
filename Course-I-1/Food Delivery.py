PRICE_CHICKEN_MENU = 10.35
PRICE_FISH_MENU = 12.40
PRICE_VEGAN_MENU = 8.15
PRICE_DELIVERY = 2.50

chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())

sum_chicken = chicken_menus * PRICE_CHICKEN_MENU
sum_fish = fish_menus * PRICE_FISH_MENU
sum_vegan = vegan_menus * PRICE_VEGAN_MENU
sum_menus = sum_fish + sum_vegan + sum_chicken
sum_desert = sum_menus * 0.2
total_sum = sum_desert + sum_menus + PRICE_DELIVERY

print(total_sum)
