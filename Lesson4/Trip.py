budget = float(input())
season = input().lower()

destination_result = 'Europe'
money_spent = 0.9 * budget
holiday_information = f"Hotel - {money_spent:.2f}"

if 100 < budget <= 1000:
    destination_result = 'Balkans'
    if season == 'summer':
        money_spent = 0.4 * budget
        holiday_information = f"Camp - {money_spent:.2f}"
    else:
        money_spent = 0.8 * budget
        holiday_information = f"Hotel - {money_spent:.2f}"
elif budget <= 100:
    destination_result = 'Bulgaria'
    if season == 'summer':
        money_spent = 0.3 * budget
        holiday_information = f"Camp - {money_spent:.2f}"
    else:
        money_spent = 0.7 * budget
        holiday_information = f"Hotel - {money_spent:.2f}"

print('Somewhere in ' + destination_result)
print(holiday_information)
