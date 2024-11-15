n = int(input())
n = str(n)
first_digit = int(n[0])
second_digit = int(n[1])
third_digit = int(n[2])

row = int(first_digit + second_digit)
col = int(first_digit + third_digit)
n = int(n)

for i in range(1, row + 1):
    for j in range(1, col + 1):

        if n % 5 == 0:
            n -= first_digit

        elif n % 3 == 0:
            n -= second_digit
        else:
            n += third_digit

        print(f'{n}', end="" + " ")
    print()
