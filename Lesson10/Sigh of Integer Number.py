def print_sign(n):
    if n > 0:
        print(f'The number {n} is positive.')
    elif n < 0:
        print(f'The number {n} is negative.')
    else:
        print(f'The number {n} is zero.')


print_sign(int(input()))
