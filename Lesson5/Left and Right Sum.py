import math

n = int(input())
sum_nums_l = 0
sum_nums_r = 0

for i in range(0,n):
    current_number = float(input())
    sum_nums_l += current_number

sum_nums_r = 0

for i in range(0,n):
    current_number = float(input())
    sum_nums_r += current_number

if sum_nums_r == sum_nums_l:
    print(f'Yes, sum = {sum_nums_r}')
 #   print(f'Yes, sum = ' + str(sum_nums_r))
  #  print(f'Yes, sum = %f' % (sum_nums_r))
else:
    print(f'No, diff = {math.fabs(sum_nums_r - sum_nums_l)}')
