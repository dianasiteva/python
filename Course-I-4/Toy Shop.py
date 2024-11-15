PRISE_PUZZLE = 2.60
PRISE_DOLL = 3
PRISE_BEAR = 4.10
PRISE_MINION = 8.20
PRISE_TRUCK = 2

trip_prise = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

total_sum = (puzzles * PRISE_PUZZLE + dolls * PRISE_DOLL + teddy_bears * PRISE_BEAR
             + minions * PRISE_MINION + trucks * PRISE_TRUCK)

if (puzzles + dolls + teddy_bears + minions + trucks) >= 50:
    total_sum -= total_sum * 0.25

total_sum -= total_sum * 0.1
result = abs(total_sum - trip_prise)

if trip_prise <= total_sum:
    print(f'Yes! {result:.2f} lv left.')
else:
    print(f'Not enough money! {result:.2f} lv needed.')
