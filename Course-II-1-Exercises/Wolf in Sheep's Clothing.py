queue = input()
tail_list = queue.split(', ')
j = 0

for i in reversed(tail_list):
    j += 1
    if i == 'wolf':
        if j == 1:
            print('Please go away and stop eating my sheep')
        else:
            print(f'Oi! Sheep number {j - 1}! You are about to be eaten by a wolf!')
