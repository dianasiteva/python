name = input()
count_all = 0
count_bad = 0
total_sum = 0
grade = 0

while count_all < 12:
    grade = float(input())

    if grade < 4:
        count_bad += 1
        if count_bad > 1:
            print(f'{name} has been excluded at {count_all + 1} grade')
            break
        continue

    total_sum += grade
    count_all += 1
else:
    print(f'{name} graduated. Average grade: {(total_sum / count_all):.2f}')
