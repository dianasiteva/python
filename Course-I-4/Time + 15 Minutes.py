hour = int(input())
minutes = int(input())

total_minutes = hour * 60 + minutes + 15
next_hour = total_minutes // 60
next_minutes = total_minutes % 60

if next_hour > 23:
    next_hour -= 24

print(f'{next_hour}:{next_minutes:02}')
