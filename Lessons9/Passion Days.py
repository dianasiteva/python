budget = float(input())
command = input()

purchases = 0
price = 0

while command != 'mall.Enter':
    command = input()

command = input()

while command != 'mall.Exit':
    for action in command:
        if 'A' <= action <= 'Z':
            price = ord(action) * 0.5
            if price <= budget:
                purchases += 1
                budget -= price
        elif 'a' <= action <= 'z':
            price = ord(action) * 0.3
            if budget >= price:
                purchases += 1
                budget -= price
        elif action == '%':
            budget = budget / 2
            purchases += 1
        elif action == '*':
            budget += 10
        else:
            price = ord(action)
            if budget >= price:
                budget -= price
                purchases += 1
    command = input()

if purchases == 0:
    print(f'No purchases. Money left: {budget:.2f} lv.')
else:
    print(f'{purchases} purchases. Money left: {budget:.2f} lv.')
