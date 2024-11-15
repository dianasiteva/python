hour_exam =int(input())
min_exam = int(input())
hour_in = int(input())
min_in = int(input())
diff = 0

all_min_exam = hour_exam * 60 + min_exam
all_min_in = hour_in * 60 + min_in
diff = all_min_exam - all_min_in

if 0 <= (all_min_exam - all_min_in) <= 30:
    print('On time')
elif (all_min_exam - all_min_in) > 30:
    print('Early')
else:
    print('Late')

if all_min_exam < all_min_in:
    diff = all_min_in - all_min_exam
    if diff < 60:
        print(f'{diff} minutes after the start')
    else:
        print(f'{diff // 60}:{(diff % 60):02} hours after the start')
elif all_min_exam > all_min_in:
    diff = all_min_exam - all_min_in
    if diff < 60:
        print(f'{diff} minutes before the start')
    else:
        print(f'{diff // 60}:{(diff % 60):02} hours before the start')
