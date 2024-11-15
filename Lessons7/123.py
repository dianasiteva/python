for num in range(100, 1000):
    a = num // 10 // 10
    b = (num - a * 100) // 10
    c = num % 10
    n = a + b
    m = a + c
    print('{} {} {} {} {} {}'.format(num, a, b, c, n, m))
