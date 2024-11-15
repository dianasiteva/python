number_of_students = int(input())

number_failed_students = 0
number_average_students = 0
number_good_students = 0
number_excellent_student = 0
total_result = 0

for i in range(0, number_of_students):
    current_grade = float(input())
    if current_grade < 3:
        number_failed_students += 1
    elif current_grade < 4:
        number_average_students += 1
    elif current_grade < 5:
        number_good_students += 1
    else:
        number_excellent_student += 1

    total_result += current_grade

total_result = total_result / number_of_students

print('Top students: {0:.2f}%'.format(number_excellent_student / number_of_students * 100))
print('Between 4.00 and 4.99: {0:.2f}%'.format(number_good_students / number_of_students * 100))
print('Between 3.00 and 3.99: {0:.2f}%'.format(number_average_students / number_of_students * 100))
print('Fail: {0:.2f}%'.format(number_failed_students / number_of_students * 100))
print(f'Average: {total_result:.2f}')
