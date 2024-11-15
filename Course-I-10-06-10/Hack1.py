i = 0

while i < 10:
    with open(f'file_{i}.txt', 'w') as f:
        f.write('You have been hacked!')

        i += 1