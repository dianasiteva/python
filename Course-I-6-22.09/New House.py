type_flower = input()
number_flowers = int(input())
budget = int(input())
diff = 0
price = 0

if type_flower == 'Roses':
    price = number_flowers * 5
    if number_flowers > 80:
        price -= price * 0.1
elif type_flower == 'Dahlias':
    price = number_flowers * 3.80
    if number_flowers > 90:
        price -= price * 0.15
elif type_flower == 'Tulips':
    price = number_flowers * 2.80
    if number_flowers > 80:
        price -= price * 0.15
elif type_flower == 'Narcissus':
    price = number_flowers * 3
    if number_flowers < 120:
        price += price * 0.15
elif type_flower == 'Gladiolus':
    price = number_flowers * 2.50
    if number_flowers < 80:
        price += price * 0.20

diff = abs(budget - price)
if budget >= price:
    print(f"Hey, you have a great garden with {number_flowers} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
