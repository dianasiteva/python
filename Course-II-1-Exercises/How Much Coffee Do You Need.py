input_command = input()
number_of_coffee = 0

while input_command != "END":
    if input_command == 'coding' or input_command == 'cat' or \
        input_command == 'dog' or input_command == 'movie':
        number_of_coffee += 1
    if input_command == 'CODING' or input_command == 'CAT' or \
        input_command == 'DOG' or input_command == 'MOVIE':
        number_of_coffee += 2
    input_command = input()

if number_of_coffee > 5:
    print('You need extra sleep')
else:
    print(number_of_coffee)
