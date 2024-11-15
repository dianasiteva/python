teat_name = input()
games = int(input())
score = 0
all_goals = 0
all_goals_received = 0

for game in range(0, games):
    goals = int(input())
    goals_received = int(input())

    if goals > goals_received:
        score += 3
        all_goals += 1
    elif goals == goals_received:
        score += 1
        all_goals_received += 1

diff = all_goals - all_goals_received

if all_goals >= all_goals_received:
    print(f'{teat_name} has finished the group phase with {score} points.')
    print(f'Goal difference: {diff}.')
else:
    print(f'{teat_name} has been eliminated from the group phase.')
    print(f'Goal difference: {diff}.')




