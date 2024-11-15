n1 = int(input())
n2 = int(input())
magic = int(input())

counter = 0
flag = False

for i in range(n1, n2 + 1):
    for j in range(n1, n2 + 1):
        counter += 1
        if i + j == magic:
            print(f'Combination N:{counter} ({i} + {j} = {magic})')
            flag = True
            break
    if flag:
        break
else:
    print(f'{counter} combinations - neither equals {magic}')
