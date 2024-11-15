n = float(input())
n = round(n * 100,0)
coins = 0
while n > 0:
    if n >= 200:
        n -= 200
        coins += 1
    elif n >= 100:
        n -= 100
        coins += 1
    elif n >= 50:
        n -= 50
        coins += 1
    elif n >= 20:
        n -= 20
        coins += 1
    elif n >= 10:
        n -= 10
        coins += 1
    elif n >= 5:
        n -= 5
        coins += 1
    elif n >= 2:
        n -= 2
        coins += 1
    elif n >= 1:
        n -= 1
        coins += 1

print(coins)
