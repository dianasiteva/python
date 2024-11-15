exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

late = 'Late'
on_time = 'On time'
early = 'Early'

exam_time = exam_hours * 60 + exam_minutes
arrival_time = arrival_hours * 60 + arrival_minutes

total_munutes_difference = arrival_time - exam_time

student_arrival = late
hours_difference = 0
minutes_difference = 0

if total_munutes_difference < -30:
    student_arrival = early
elif total_munutes_difference <= 0:
    student_arrival = on_time

result = ''

if total_munutes_difference != 0:
    hours_difference = abs(total_munutes_difference) // 60
    minutes_difference = abs(total_munutes_difference) % 60

    if hours_difference > 0:
        result = f"{hours_difference}:{minutes_difference:02} hours"
    else:
        result = f"{minutes_difference} minutes"

    if total_munutes_difference < 0:
        result += ' before the start'
    else:
        result += ' after the start'

print(student_arrival)
if result != '':
    print(result)
