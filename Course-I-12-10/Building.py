floors = int(input())
rooms = int(input())

for e in range(floors, 0, -1):
    if e == floors:
        letter = 'L'
    elif e % 2 == 0:
        letter = 'O'
    else:
        letter = 'A'
    for r in range(0, rooms):
        print(f'{letter}{e}{r}', end=' ')
    print()
