import math

V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

water = (P1 + P2) * H

if water <= V:
    print('The pool is {0}% full. Pipe 1: {1}%. Pipe 2: {2}%.'.format(
        math.trunc(water / V * 100),
        math.trunc((P1 * H) / water * 100),
        math.trunc((P2 * H) / water * 100)
    ))
else:
    print('For {0} hours the pool overflows with {1} litres.'.format(
        H, water - V
    ))

