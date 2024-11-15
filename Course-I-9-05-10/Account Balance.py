in_input = input()
total_sum = 0

while in_input != 'NoMoreMoney':
    in_sum = float(in_input)
    if in_sum <= 0:
        print('Invalid operation!')
        break
    else:
        total_sum += in_sum
        print(f'Increase: {in_sum:.2f}')
    in_input = input()

print(f'Total: {total_sum:.2f}')
