first_string = input()
second_string = input()
result = ''
print_result = second_string

for i in range(0, len(first_string)):
    result = second_string[0: i + 1] + first_string[i + 1: len(first_string)]
    if print_result != result:
        print(result)
        print_result = result
