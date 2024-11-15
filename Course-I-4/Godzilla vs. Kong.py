budget = float(input())
extras = int(input())
prise = float(input())

if extras > 150:
    prise -= prise * 0.1

total_prise = extras * prise + budget * 0.1
result = abs(budget - total_prise)

if budget >= total_prise:
    print("Action!")
    print(f"Wingard starts filming with {result:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {result:.2f} leva more.")
