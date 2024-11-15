time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_third + time_second + time_first
minutes = total_time // 60
secons = total_time % 60

print(f"{minutes}:{secons:02}")
