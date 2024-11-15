import math
from math import ceil

name_episode = input()
time_episode = int(input())
time_rest = int(input())
time_lunch = time_rest / 8
time_relax = time_rest / 4

time_sum = time_relax + time_lunch + time_episode

if time_sum <= time_rest:
    diff = math.ceil(time_rest - time_sum)
    print(f'You have enough time to watch {name_episode} and left with {diff} minutes free time.')
else:
    diff = math.ceil(time_sum - time_rest)
    print(f"You don't have enough time to watch {name_episode}, you need {diff} more minutes.")
