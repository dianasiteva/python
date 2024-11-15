n = int(input())
flag = False
counter = 0
for i in range(1, n + 1):
    for j in range (1, i + 1):
        counter += 1
        print(counter, end=" ")
        if counter == n:
            flag = True
            break
    if flag:
        break
    print()
