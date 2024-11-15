import math

n = int(input())
is_prime = True

if n < 2:
    is_prime = False
else:
    for num in range(2, int(math.sqrt(n)) + 1):
        if n % num == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print('Not prime')


