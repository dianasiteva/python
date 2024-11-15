n = int(input())

suma = 0
num = 0
max_num = 0
num_sum_others = ''
nums = []

for i in range(0, n):
    num = int(input())
    suma += num
    nums.append(num)

    if i == 0:
        max_num = num
    elif max_num < num:
        max_num = num

for i in range(0, n):
    if nums[i] == suma - nums[i]:
        num_sum_others = nums[i]

if type(num_sum_others) == str:
    print('No\nDiff = ' + str(abs(max_num -(suma - max_num))))
else:
    print('Yes\nSum = ' + str(num_sum_others))
