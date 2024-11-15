deposit = float(input())
term = int(input())
percent = float(input()) / 100

sum_amount = deposit  + term * ((deposit * percent ) / 12)

print(sum_amount)
