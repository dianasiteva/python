n = int(input())
counter = 0

for name_s in range(ord('B'), ord('L') + 2):   # B e 4etno w ascii
    for sector in range(ord('f'), ord('a') - 1, -1):
        for entrance in range(ord('A'), ord('C') + 1):
            for row_num in range(1, 11):
                for seat in range(10, 0, -1):
                    counter += 1
                    if counter == n:
                        sum = name_s + sector + entrance + row_num + seat
                        print(f'Ticket combination: {chr(name_s)}{chr(sector)}{chr(entrance)}{row_num}{seat}')
                        print(f'Price: {sum} lv.')
