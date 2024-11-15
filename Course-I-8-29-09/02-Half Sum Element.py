n = int(input())
sum_numbers = 0
max_number = 0

for num in range(n):
    number = int(input())
    sum_numbers += number
    if num == 0:
        max_number = number
    else:
        if max_number < number:
            max_number = number

if sum_numbers - max_number == max_number:
    print(f'Yes\nSum = {max_number}')
else:
    print(f'No\nDiff = {abs(max_number - (sum_numbers - max_number))}')
