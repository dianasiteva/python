day = int(input())
month = int(input())

days_in_month = 31

if month == 2:
    days_in_month = 28

if month == 4 or month == 6 or month == 9 or month == 11:
    days_in_month = 30

day += 5

if day > days_in_month:
    month += 1
    day -= days_in_month

if month > 12:
    month = 1

print(f"{day}.{month:02}")
