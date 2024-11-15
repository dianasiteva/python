n = int(input())
sum1 = sum2 = sum3 = 0

for i in range(0, n):
    num = int(input())
    if i % 3 == 0:
        sum1 += num
    if i % 3 == 1:
        sum2 += num
    if i % 3 == 2:
        sum3 += num

print('sum1 = %d' % sum1)
print('sum2 = %d' % sum2)
print('sum3 = %d' % sum3)
