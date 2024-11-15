import math
from math import floor

record = float(input())
distance = float(input())
seconds_per_meter = float(input())

seconds_for_distance = distance * seconds_per_meter
delay_times = math.floor(distance / 15)
result = seconds_for_distance + delay_times * 12.5
diff = abs(record - result)

if result < record:
    print(f'Yes, he succeeded! The new world record is {result:.2f} seconds.')
else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')
