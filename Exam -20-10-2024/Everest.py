top = 8848
total_m = 5364
days = 1
flag = False

while True:

    command = input().lower()
    if command == 'end':
        break

    m_per_day = int(input())

    if command == 'yes':
        if days + 1 > 5:
            break
        days += 1
        total_m += m_per_day
    elif command == 'no':
        total_m += m_per_day

    if total_m >= top:
        flag = True
        break

if flag:
    print(f'Goal reached for {days} days!')
else:
    print('Failed!')
    print(f'{total_m}')
