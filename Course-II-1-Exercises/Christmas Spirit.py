quantity_of_decorations = int(input())
days_left = int(input())
money_need = 0
spirit = 0
decorate = quantity_of_decorations

for i in range(1, days_left + 1):
    if i % 11 == 0:
        decorate += 2
    if i % 2 == 0:
        money_need += 2 * decorate
        spirit += 5
    if i % 3 == 0:
        money_need += (5 + 3) * decorate
        spirit += (3 + 10)
    if i % 5 == 0:
        money_need += 15 * decorate
        spirit += 17
    if i % 3 == 0 and i % 5 == 0:
        spirit += 30
    if i % 10 == 0:
        spirit -= 20
        money_need += 5 + 3 + 15
        if i == days_left:
            spirit -= 30

print(f'Total cost: {money_need}')
print(f'Total spirit: {spirit}')
