import math

budget = float(input())
house = float(input())
windows = int(input())
styr = float(input())
price = float(input())

area = house - windows * 2.4 + 0.1 * (house - windows * 2.4)
sumata = math.ceil(area / styr) * price

if budget >= sumata:
    diff = budget - sumata
    print(f"Spent: {sumata:.2f}")
    print(f"Left: {diff:.2f}")
else:
    diff = sumata - budget
    print(f"Need more: {diff:.2f}")
