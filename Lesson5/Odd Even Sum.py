n = int(input())

odd_sum = 0
even_sum = 0
num = 0

for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
if even_sum == odd_sum:
    print('Yes')
    print('Sum = ' + str(even_sum))
else:
    print('No')
    print('Diff = ' + str(abs(even_sum - odd_sum)))

