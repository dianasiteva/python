input_string = input()

while input_string != "End":
    if not input_string == "SoftUni":

        for i in range(0, len(input_string)):
            print(input_string[i] * 2, end='')

        print()
    input_string = input()
