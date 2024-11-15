width = int(input())
height = int(input())

area = width * height

data = input()

while not data == "STOP":
    area -= int(data)
    if area < 0:
        print(f"No more cake left! You need {abs(area)} pieces more.")
        break
    data = input()

if area > 0:
    print(f"{area} pieces are left.")
