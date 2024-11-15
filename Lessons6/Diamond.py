n = int(input())

left_right = (n - 1) // 2


for i in range(0, (n + 1) // 2):
    print('-' * left_right + '*', end='')
    mid = n - 2 * left_right - 2
    if mid >= 0:
        print('-' * mid + '*', end='')
    print('-' * left_right)
    left_right -= 1

left_right = 0

for i in range(0, (n - 1) // 2):
    left_right += 1
    print('-' * left_right + '*', end='')
    mid = n - 2 * left_right - 2
    if mid >= 0:
        print('-' * mid + '*', end='')
    print('-' * left_right)
