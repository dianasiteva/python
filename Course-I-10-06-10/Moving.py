length = int(input())
width = int(input())
height = int(input())
space = width * height * length
diff = 0
in_input = input()

while in_input != 'Done':
    boxes = int(in_input)
    diff = space - boxes
    if diff < 0:
        print(f'No more free space! You need {abs(diff)} Cubic meters more.')
        break
    if diff == 0:
        break
    space = diff
    in_input = input()
else:
    print(f'{diff} Cubic meters left.')
