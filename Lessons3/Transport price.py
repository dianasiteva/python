distance = int(input())
day_or_night = input()
price = 0.0
taxi_rate = 0.0

if day_or_night == "day":
    taxi_rate = 0.79
else:
    taxi_rate = 0.90

if distance < 20:
    price = 0.70 + taxi_rate * distance
elif distance < 100:
    price = distance * 0.09
else:
    price = distance * 0.06

print('%.2f' % price)
