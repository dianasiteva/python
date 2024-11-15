c1 = int(input())
c2 = int(input())
c3 = int(input())
ss = c1 + c2 + c3
mm = 0

if ss > 59:
    mm += 1
    ss -= 60

if ss > 59:
    mm += 1
    ss -=60

if ss < 10:
    print(f'{mm}:0{ss}')
else:
    print(f'{mm}:{ss}')
