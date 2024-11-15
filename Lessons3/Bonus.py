t = int(input())
bonus = 0

if t < 100:
    bonus += 5
elif t > 1000:
    bonus += t * 0.1
else:
    bonus += t * 0.2

if t % 2 == 0:
    bonus += 1

if t % 10 == 5:
    bonus += 2

print("Enter score: " + str(t))
print("Bonus score: " + str(bonus))
print("Total score: " + str(t + bonus))
