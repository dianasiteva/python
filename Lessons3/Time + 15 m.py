h = int(input())
m = int(input())

if m + 15 > 59:
    h += 1
    m += (15 - 60)
else:
    m += 15

if h > 23:
    h -= 24

if m < 10:
    print(f"{h}:0{m}")
else:
    print(f"{h}:{m}")

