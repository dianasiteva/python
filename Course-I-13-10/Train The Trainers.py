n = int(input())
name = input()
counter = 0
sum_all = 0

while name != 'Finish':
    sum_name = 0
    counter += 1

    for i in range(0, n):
        grade = float(input())
        sum_name += grade

    print(f"{name} - {(sum_name / n):.2f}.")
    sum_all += (sum_name / n)
    name = input()

print(f"Student's final assessment is {(sum_all / counter):.2f}.")
