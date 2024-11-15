num = int(input())
a = num // 10 // 10
b = (num - a * 100) // 10
c = num % 10
n = a + b
m = a + c

for i in range(1, n + 1):
    j = 1
    while j <= m:
        if num % 5 == 0:
            num -= a
            print(num, end=' ')
            j += 1
            if j > m:
                print()
                break
        if num % 3 == 0:
            num -= b
            print(num, end=' ')
            j += 1
            if j > m:
                print()
                break
        if num % 5 != 0 and num % 3 != 0:
            num += c
            print(num, end=' ')
            j += 1
            if j > m:
                print()
                break
