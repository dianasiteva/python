actor_name = input()
starting_academy_points = float(input())
number_judges = int(input())

result = starting_academy_points

for _ in range(number_judges):
    judge_name = input()
    judge_points = float(input())
    result += len(judge_name) * judge_points / 2
    if result > 1250.5:
        break

if result > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {result:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {(1250.5 - result):.1f} more!')
