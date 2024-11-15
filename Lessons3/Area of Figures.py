import math

vid = input().lower()

if vid == "square":
    sq = float(input())
    print('%.3f' % (sq * sq))
if vid == "rectangle":
    reca = float(input())
    recb = float(input())
    print("%.3f" % (reca * recb))
if vid == "circle":
    r =float(input())
    print("%.3f" % (math.pi * r * r))
if vid == "triangle":
    tra = float(input())
    trh = float(input())
    print("%.3f" % (tra * trh / 2))
