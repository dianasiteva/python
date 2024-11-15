n = int(input('n = '))
max_num = 0

for i in range(0, n):
    num = int(input())
    if i == 0:
        max_num = num
    elif num > max_num:
        max_num = num

print('max = ' + str(max_num))
