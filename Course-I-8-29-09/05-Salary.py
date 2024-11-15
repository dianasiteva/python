n = int(input())
salary = int(input())

for i in range(n):
    name_site = input()
    if name_site == 'Facebook':
        salary -= 150
    elif name_site == 'Instagram':
        salary -= 100
    elif name_site == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(f'{int(salary)}')
