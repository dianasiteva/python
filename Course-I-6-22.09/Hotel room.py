month = input()
days = int(input())
studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if 7 < days <= 14:
        studio -= studio * 0.05
    if days > 14:
        studio -= studio * 0.3
        apartment -= apartment * 0.1
elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    if days > 14:
        studio -= studio * 0.2
        apartment -= apartment * 0.1
elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    if days > 14:
        apartment -= apartment * 0.1

print(f'Apartment: {(apartment * days):.2f} lv.')
print(f'Studio: {(studio * days):.2f} lv.')
