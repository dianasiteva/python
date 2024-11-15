people = int(input())
nights = int(input())
cards = int(input())
tickets = int(input())

total_sum = (nights * 20 + cards * 1.6 + tickets * 6) * people
total_sum += total_sum * 0.25

print(f'{total_sum:.2f}')
