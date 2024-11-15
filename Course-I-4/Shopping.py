budget = float(input())
n = int(input())
m = int(input())
p = int(input())
n_prise = 250
m_prise = n * n_prise * 0.35
p_prise = n * n_prise * 0.1
total_sum = n * n_prise + m * m_prise + p * p_prise

if n > m:
    total_sum -= total_sum * 0.15

diff = abs(budget - total_sum)

if total_sum > budget:
    print(f'Not enough money! You need {diff:.2f} leva more!')
else:
    print(f'You have {diff:.2f} leva left!')
