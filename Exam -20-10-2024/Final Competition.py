bg_summer_percent = 0.05
bg_winter_percent = 0.08
foreign_summer_percent = 0.1
foreign_winter_percent = 0.15

people = int(input())
score = float(input())
season = input()
place = input()
money_prise_person = 0
money_prise = 0

total_money_prise = 0

if place == 'Bulgaria':
    money_prise = people * score
    if season == 'summer':
        money_prise -= money_prise * bg_summer_percent
    elif season == 'winter':
        money_prise -= money_prise * bg_winter_percent
elif place == 'Abroad':
    money_prise = people * score * 1.5
    if season == 'summer':
        money_prise -= money_prise * foreign_summer_percent
    elif season == 'winter':
        money_prise -= money_prise * foreign_winter_percent

charity = money_prise * 0.75
total_money_prise = money_prise - charity

money_prise_person = total_money_prise / people

print(f'Charity - {charity:.2f}')
print(f'Money per dancer - {money_prise_person:.2f}')
