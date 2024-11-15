n = int(input())
even_sum = 0
odd_sum = 0

for i in range(0, n):
    if i % 2 == 0:
        even_sum += int(input())
    else:
        odd_sum += int(input())

diff = abs(even_sum - odd_sum)

if diff == 0:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    print('No')
    print(f'Diff = {diff}')
