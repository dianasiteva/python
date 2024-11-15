days = int(input())
type_room = input()
grade = input()
price = 0

if type_room == 'room for one person':
    price = (days - 1) * 18
elif type_room == 'apartment':
    price = (days - 1) * 25
    if days < 10:
        price -= price * 0.3
    elif days > 15:
        price -= price * 0.5
    else:
        price -= price * 0.35
elif type_room == 'president apartment':
    price = (days - 1) * 35
    if days < 10:
        price -= price * 0.1
    elif days > 15:
        price -= price * 0.2
    else:
        price -= price * 0.15

if grade == 'positive':
    price += price * 0.25
else:
    price -= price * 0.1

print(f'{price:.2f}')
