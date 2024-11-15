allowed_bad_grades = int(input())
task_numbers = 0
bad_grades = 0
sum_grades = 0
last_task = ''
task_name = input()

while task_name != 'Enough':
    grade = int(input())
    if grade <= 4:
        bad_grades += 1
        if bad_grades >= allowed_bad_grades:
            print(f'You need a break, {bad_grades} poor grades.')
            break
    sum_grades += grade
    task_numbers += 1
    last_task = task_name
    task_name = input()
else:
    print(f'Average score: {(sum_grades / task_numbers):.2f}')
    print(f'Number of problems: {task_numbers}')
    print(f'Last problem: {last_task}')
