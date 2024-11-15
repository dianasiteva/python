n = int(input())

for i in range(1111, 10000):
    flag = True
    for ind, num in enumerate(str(i)):
        if num == '0':
            flag = False
            break
        if n % int(num) != 0:
            flag = False
            break
    if flag:
        print(i, end=" ")
