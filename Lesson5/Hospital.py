period = int(input())
treated_patients = 0
untreated_patients = 0
count_of_doctors = 7
patients = 0

for i in range(1, period + 1):
    patients = int(input())

    if (i % 3 == 0) and (untreated_patients > treated_patients):
        count_of_doctors += 1

    if patients > count_of_doctors:
        treated_patients += count_of_doctors
        untreated_patients += patients - count_of_doctors
    else:
        treated_patients += patients

print('Treated patients: ' + str(treated_patients) + '.')
print('Untreated patients: ' + str(untreated_patients) + '.')
