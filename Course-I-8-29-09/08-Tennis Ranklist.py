from math import floor

win_points = 2000
semi_final_points = 720
final_points = 1200
number_wins = 0
points = 0

number_tourneys = int(input())
starting_points = int(input())

for _ in range(number_tourneys):
    part_of_tourney = input()
    if part_of_tourney == 'W':
        points += win_points
        number_wins += 1
    elif part_of_tourney == 'F':
        points += final_points
    elif part_of_tourney == 'SF':
        points += semi_final_points

print(f'Final points: {starting_points + points}')
print(f'Average points: {floor(points / number_tourneys)}')
print(f'{(number_wins / number_tourneys * 100):.2f}%')
