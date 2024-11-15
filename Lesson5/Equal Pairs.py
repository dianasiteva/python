n = int(input())
sum_of_pair = 0
sum_of_previous = 0
num = 0
diff = 0

for i in range(0, 2 * n):
    num = int(input())
    sum_of_pair += num
    if i % 2 != 0:
        if i == 1:
            sum_of_previous = sum_of_pair
            sum_of_pair = 0
        elif diff != sum_of_pair - sum_of_previous:
            diff = sum_of_pair - sum_of_previous
            sum_of_previous = sum_of_pair
            sum_of_pair = 0
        else:
            sum_of_previous = sum_of_pair
            sum_of_pair = 0

if diff == 0:
    print('Yes, value=' + str(sum_of_previous))
else:
    print('No, maxdiff=' + str(abs(diff)))
