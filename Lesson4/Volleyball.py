import math

year = input().lower()
holidays = int(input())
weekends_home = int(input())

Sofia_weekends = 48 - weekends_home
play_Sofia = Sofia_weekends * 3 / 4 + holidays * 2 / 3
play_total = play_Sofia + weekends_home

if year == 'leap':
    print(math.floor(play_total * 15 / 100 + play_total))
else:
    print(math.floor(play_total))
