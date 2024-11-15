width = int(input())
length = int(input())

all_pieces = width * length
diff = 0
in_input = input().upper()

while in_input != 'STOP':
    pieces = int(in_input)
    diff = all_pieces - pieces
    if diff < 0:
        print(f'No more cake left! You need {abs(diff)} pieces more.')
        break
    if diff == 0:
        break
    all_pieces -= pieces
    in_input = input().upper()
else:
    print(f'{all_pieces} pieces are left.')
