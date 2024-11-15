inheritance = float(input())
year_to_live = int(input())
years = 18

for i in range(1800, year_to_live + 1):
    if i % 2 == 0:
        inheritance -= 12000
    else:
        inheritance -= (12000 + 50 * years)
    years += 1

if inheritance < 0:
    print('He will need %.2f dollars to survive.' % abs(inheritance))
else:
    print('Yes! He will live a carefree life and will have %.2f dollars left.' % inheritance)
