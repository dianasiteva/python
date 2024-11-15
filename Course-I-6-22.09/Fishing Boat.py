budget = int(input())
season = input()
fishing_men = int(input())
price = 0

if season == 'Winter':
    price = 2600
elif season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200

if fishing_men <= 6:
    price -= price * 0.1
elif fishing_men >= 12:
    price -= price * 0.25
else:
    price -= price * 0.15

if season != 'Autumn' and fishing_men % 2 == 0:
    price -= price * 0.05

if budget >= price:
    print(f'Yes! You have {(budget - price):.2f} leva left.')
else:
    print(f'Not enough money! You need {(price - budget):.2f} leva.')
