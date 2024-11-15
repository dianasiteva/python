import math

x = int(input())
w = int(input())
m = int(input())

bricks_in_course = w * m
total_courses = math.ceil(x / bricks_in_course)

print(total_courses)
