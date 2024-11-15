goal = 10000
in_input = input()
steps = 0

while in_input != 'Going home':
    steps += int(in_input)
    if steps >= goal:
        print('Goal reached! Good job!')
        print(f'{steps - goal} steps over the goal!')
        break
    in_input = input()
else:
    steps += int(input())
    if steps < goal:
        print(f'{goal - steps} more steps to reach goal.')
    else:
        print('Goal reached! Good job!')
        print(f'{steps - goal} steps over the goal!')
