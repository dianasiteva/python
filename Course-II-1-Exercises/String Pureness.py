n = int(input())

for i in range(0, n):
    input_string = input()
    if "," in input_string or \
            "." in input_string or \
            "_" in input_string:
        print(f'{input_string} is not pure!')
    else:
        print(f'{input_string} is pure.')
