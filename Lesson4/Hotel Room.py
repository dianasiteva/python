month = input().lower()
nights = int(input())

studio_price = 50.00
apartment_price = 65.00
studio_rent = 0
apartment_rent = 0

if month == 'may' or month == 'october':
    studio_price = 50.00
    apartment_price = 65.00
    studio_rent = studio_price * nights
    apartment_rent = apartment_price * nights
    if nights > 14:
        studio_rent *= 0.70
        apartment_rent *= 0.90
    elif nights > 7:
        studio_rent *= 0.95

elif month == 'june' or month == 'september':
    studio_price = 75.20
    apartment_price = 68.70
    studio_rent = studio_price * nights
    apartment_rent = apartment_price * nights
    if nights > 14:
        studio_rent *= 0.80
        apartment_rent *= 0.90
if month == 'july' or month == 'august':
    studio_price = 76.00
    apartment_price = 77.00
    studio_rent = studio_price * nights
    apartment_rent = apartment_price * nights
    if nights > 14:
        apartment_rent *= 0.90

studio_info = f'Studio: {studio_rent:.2f} lv.'
apartment_info = f'Apartment: {apartment_rent:.2f} lv.'

print(apartment_info)
print(studio_info)
