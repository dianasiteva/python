n1 = int(input())
n2 = int(input())
action = input()
result = 0

if action == '+' or action == '-' or action == '*':
    if action == '+':
        result = n1 + n2
    elif action == '-':
        result = n1 - n2
    else:
        result = n1 * n2

    if result % 2 == 0:
        print(f'{n1} {action} {n2} = {result} - even')
    else:
        print(f'{n1} {action} {n2} = {result } - odd')

if action == '/':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 / n2
        print(f'{n1} / {n2} = {result:.2f}')

if action == '%':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 % n2
        print(f'{n1} % {n2} = {result}')
