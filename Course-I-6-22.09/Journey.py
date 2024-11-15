budget = float(input())
season = input()
place = ''
type_rest = ''
price = 0

if budget <= 100:
    place = 'Bulgaria'
    if season == 'summer':
        price = 0.3 * budget
        type_rest = 'Camp'
    elif season == 'winter':
        price = 0.7 * budget
        type_rest = 'Hotel'
elif budget > 1000:
    price = 0.9 * budget
    place = 'Europe'
    type_rest = 'Hotel'
else:
    place = 'Balkans'
    if season == 'summer':
        price = 0.4 * budget
        type_rest = 'Camp'
    elif season == 'winter':
        price = 0.8 * budget
        type_rest = 'Hotel'

print(f'Somewhere in {place}')
print(f'{type_rest} - {price:.2f}')
