import math

holidays = int(input())
to_play = holidays * 127 + (365 - holidays) * 63
diference = math.fabs(30000 - to_play)
hours = int(diference // 60)
minutes = int(diference % 60)

if to_play > 30000:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
