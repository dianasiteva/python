budget = float(input())
ticket_type = input().lower()
people = int(input())

transport_charges = 0
money_for_tickets = 0
money_difference = 0

if people <= 4:
    transport_charges = 0.75 * budget
elif people <= 9:
    transport_charges = 0.60 * budget
elif people <= 24:
    transport_charges = 0.50 * budget
elif people <= 49:
    transport_charges = 0.40 * budget
elif people >= 50:
    transport_charges = 0.25 * budget

if ticket_type == 'normal':
    money_for_tickets = people * 249.99
elif ticket_type == 'vip':
    money_for_tickets = people * 499.99

money_difference = budget - money_for_tickets - transport_charges
result = f'Yes! You have {money_difference:.2f} leva left.'

if money_difference < 0:
    result = f'Not enough money! You need {abs(money_difference):.2f} leva.'

print(result)
