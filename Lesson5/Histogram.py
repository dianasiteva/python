n= int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
cnt_p1 = 0
cnt_p2 = 0
cnt_p3 = 0
cnt_p4 = 0
cnt_p5 = 0

for i in range(0, n):
    num = int(input())
    if num < 200:
        cnt_p1 += 1
    elif 200 <= num < 400:
        cnt_p2 += 1
    elif 400 <= num < 600:
        cnt_p3 += 1
    elif 600 <= num < 800:
        cnt_p4 += 1
    else:
        cnt_p5 += 1

p1 = cnt_p1 * 100 / n
p2 = cnt_p2 * 100 / n
p3 = cnt_p3 * 100 / n
p4 = cnt_p4 * 100 / n
p5 = cnt_p5 * 100 / n

print('%.2f' % p1 + '%')
print('%.2f' % p2 + '%')
print('%.2f' % p3 + '%')
print('%.2f' % p4 + '%')
print('%.2f' % p5 + '%')