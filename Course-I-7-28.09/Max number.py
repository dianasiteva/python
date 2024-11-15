max_number = 0
n = int(input())

for num in range(n):
    number = int(input())
    if num == 0:
        max_number = number
    else:
        if max_number < number:
            max_number = number

print(max_number)
