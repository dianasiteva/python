team = input().lower()
souvenir = input().lower()
count_souvenirs = int(input())
total_sum = None

if souvenir == 'flags' or souvenir == 'caps' or souvenir == 'stikers' or souvenir == 'posters':
    if team == 'argentina':
        if souvenir == 'flags':
            total_sum = 3.25 * count_souvenirs
        elif souvenir == 'caps':
            total_sum = 7.20 * count_souvenirs
        elif souvenir == 'posters':
            total_sum = 5.10 * count_souvenirs
        elif souvenir == 'stikers':
            total_sum = 1.25 * count_souvenirs
    elif team == 'brazil':
        if souvenir == 'flags':
            total_sum = 4.20 * count_souvenirs
        elif souvenir == 'caps':
            total_sum = 8.50 * count_souvenirs
        elif souvenir == 'posters':
            total_sum = 5.35 * count_souvenirs
        elif souvenir == 'stikers':
            total_sum = 1.20 * count_souvenirs
    elif team == 'croatia':
        if souvenir == 'flags':
            total_sum = 2.75 * count_souvenirs
        elif souvenir == 'caps':
            total_sum = 6.90 * count_souvenirs
        elif souvenir == 'posters':
            total_sum = 4.95 * count_souvenirs
        elif souvenir == 'stikers':
            total_sum = 1.10 * count_souvenirs
    elif team == 'denmark':
        if souvenir == 'flags':
            total_sum = 3.10 * count_souvenirs
        elif souvenir == 'caps':
            total_sum = 6.50 * count_souvenirs
        elif souvenir == 'posters':
            total_sum = 4.80 * count_souvenirs
        elif souvenir == 'stikers':
            total_sum = 0.90 * count_souvenirs
    else:
        print('Invalid country!')
else:
    print('Invalid souvenir!')

if total_sum != None:
    print(f'{total_sum:.2f}')
