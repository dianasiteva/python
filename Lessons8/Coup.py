n = int(input())
width = 5 * n
dots = n
hashtags = width - 2 * dots
for i in range(1, n // 2 + 1):
    print("." * dots + '#' * hashtags + '.' * dots)
    dots = dots + 1
    hashtags = width - 2 * dots

middle_dots = width - 2 - 2 * dots

for i in range(1, n//2 + 2):
    print('.' * dots + '#' + '.' * middle_dots +'#' + '.' * dots)
    dots += 1
    middle_dots -= 2

dots -= 1
middle_dots += 4
print('.' * dots + '#' * middle_dots + '.' * dots)

dots -= 2
middle_dots += 4

for i in range(1, n//2 + 1):
    print('.' * dots + '#' * middle_dots + '.' * dots)

static_row = (width - 10) // 2
print('.' * static_row + 'D^A^N^C^E^' + '.' * static_row)

for i in range(1, n//2 + 2):
    print('.' * dots + '#' * middle_dots + '.' * dots)
