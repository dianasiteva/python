n = int(input('n = '))
min_num = 0

for i in range(0, n):
    num = int(input())
    if i == 0:
        min_num = num
    elif num < min_num:
        min_num = num

print('min = ' + str(min_num))
