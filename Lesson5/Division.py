n = int(input())
divisible_by_2 = 0
divisible_by_3 = 0
divisible_by_4 = 0

for i in range(0, n):
    num = int(input())
    if num % 2 == 0:
        divisible_by_2 += 1
    if num % 3 == 0:
        divisible_by_3 += 1
    if num % 4 == 0:
        divisible_by_4 += 1

print('%.2f' % (divisible_by_2 * 100 / n) + '%')
print('%.2f' % (divisible_by_3 * 100 / n) + '%')
print('%.2f' % (divisible_by_4 * 100 / n) + '%')
