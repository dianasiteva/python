change = float(input())
coins = 0
diff = int(change * 100)
middle_sum = 0

while diff > 0:
    if diff >= 200:
        middle_sum = diff % 200
        coins += diff // 200
        diff = middle_sum
    if diff >= 100:
        middle_sum = diff % 100
        coins += diff // 100
        diff = middle_sum
    if diff >= 50:
        middle_sum = diff % 50
        coins += diff // 50
        diff = middle_sum
    if diff >= 20:
        middle_sum = diff % 20
        coins += diff // 20
        diff = middle_sum
    if diff >= 10:
        middle_sum = diff % 10
        coins += diff // 10
        diff = middle_sum
    if diff >= 5:
        middle_sum = diff % 5
        coins += diff // 5
        diff = middle_sum
    if diff >= 2:
        middle_sum = diff % 2
        coins += diff // 2
        diff = middle_sum
    if diff >= 1:
        coins += diff
        diff = 0
    print(coins)
