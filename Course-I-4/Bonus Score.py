scores = int(input())
points = 0

if scores <= 100:
    points = 5
elif scores > 1000:
    points = scores * 0.1
else:
    points = scores * 0.2

if scores % 2 == 0:
    points += 1
if scores % 10 == 5:
    points += 2

print(points)
print(points + scores)
