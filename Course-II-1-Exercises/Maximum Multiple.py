n = int(input())
boundary = int(input())

for i in range(boundary, 0, -1):
    if i % n == 0:
        print(i)
        break
