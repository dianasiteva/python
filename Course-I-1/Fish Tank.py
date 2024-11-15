a = int(input())
b = int(input())
h = int(input())
percent = float(input()) / 100

v = a * b * h / 1000
used_v = v - v * percent
print(used_v)
