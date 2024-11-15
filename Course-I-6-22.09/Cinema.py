type_movie = input()
rows = int(input())
cols = int(input())
seats = rows * cols
price = 0

if type_movie == 'Premiere':
    price = seats * 12
elif type_movie == 'Normal':
    price = seats * 7.5
elif type_movie == 'Discount':
    price = seats * 5

print(f'{price:.2f} leva')
