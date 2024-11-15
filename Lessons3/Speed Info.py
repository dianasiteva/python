speed = float(input())

if speed <= 10:
    print("slow")
elif speed > 1000:
    print("extremely fast")
elif speed > 150:
    print("ultra fast")
elif speed > 50:
    print("fast")
else:
    print("average")
