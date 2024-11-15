rose_autumn_winter_price = 4.50
rose_spring_summer_price = 4.10
tulip_autumn_winter_price = 4.15
tulip_spring_summer_price = 2.50
chrysantemum_autumn_winter_price = 3.75
chrysantemum_spring_summer_price = 2.00
arrange_price = 2.00
price_increase_persentage = 15
tulip_price_decrease_persentage = 5
rose_price_decrease_persentage = 10
total_price_decrease_persentage = 20
tulip_price_decrease_threshold = 7
rose_price_decrease_threshold = 10
total_price_decrease_threshold = 20

chrysantemums_purchased = int(input())
roses_purchased = int(input())
tulips_purchased = int(input())
season = input().lower()
is_special_day = input().lower()

if season == 'winter' or season == 'autumn':
    rose_price = roses_purchased * rose_autumn_winter_price
    tulip_price = tulips_purchased * tulip_autumn_winter_price
    chrysantemum_price = chrysantemums_purchased * chrysantemum_autumn_winter_price
    total_price = rose_price + tulip_price + chrysantemum_price
else:
    rose_price = roses_purchased * rose_spring_summer_price
    tulip_price = tulips_purchased * tulip_spring_summer_price
    chrysantemum_price = chrysantemums_purchased * chrysantemum_spring_summer_price
    total_price = rose_price + tulip_price + chrysantemum_price

if is_special_day == 'y':
    total_price += total_price * price_increase_persentage / 100

if season == 'spring' and tulips_purchased > tulip_price_decrease_threshold:
    total_price -= tulip_price_decrease_persentage * total_price / 100

if season == 'winter' and roses_purchased >= rose_price_decrease_threshold:
    total_price -= rose_price_decrease_persentage * total_price / 100

if (roses_purchased + tulips_purchased + chrysantemums_purchased) > total_price_decrease_threshold:
    total_price -= total_price * total_price_decrease_persentage / 100

total_price += arrange_price

print(f"{total_price:.2f}")
