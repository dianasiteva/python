n = int(input())
count_current = count = a_prev = 0

for i in range(0, n):
    a = int(input())
    if a > a_prev:
        count_current += 1
    else:
        count_current = 1

    if count_current > count:
        count = count_current

    a_prev = a

print(count)
