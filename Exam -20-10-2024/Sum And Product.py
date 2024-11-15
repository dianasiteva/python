n = input()
out_print = ''
flag = False

for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):
                sum_abcd = a + b + c + d
                pro_abcd = a * b * c * d
                end_n = n[-1]
                if end_n == '5' and sum_abcd == pro_abcd:
                    print(str(a) + str(b) + str(c) + str(d))
                    flag = True
                    break
                if pro_abcd // sum_abcd == 3 and int(n) % 3 == 0:
                    print(str(d) + str(c) + str(b) + str(a))
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break

if not flag:
    print('Nothing found')
