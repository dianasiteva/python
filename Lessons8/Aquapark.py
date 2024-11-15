month = input().lower()
hours = int(input())
people = int(input())
day_or_night = input().lower()

result = 0

if month == "march" or month == "april" or month == "may":
    if day_or_night == "day":
        result = 10.50
    else:
        result = 8.40
elif month == "june" or month == "july" or month == "august":
    if day_or_night == "day":
        result = 12.60
    else:
        result = 10.20

if people >= 4:
    result = 0.9 * result
if hours >= 5:
    result = result * 0.5

sum = result * people * hours

print(f"Price per person for ine hour: {result:.2f}")
print(f"Total cost of the visit: {sum:.2f}")
