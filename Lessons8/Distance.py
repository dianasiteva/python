first_speed = int(input())
time1 = int(input())
time2 = int(input())
time3 = int(input())

km = 0

km += first_speed * time1 / 60
km += 1.1 * first_speed * time2 / 60
km += (1.1 * first_speed) * 0.95 * time3 / 60

print(f"{km:.2f}")
