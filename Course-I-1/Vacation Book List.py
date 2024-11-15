page_numbers = int(input())
pages_per_hour = int(input())
days = int(input())

pages_per_day = page_numbers // pages_per_hour
hours = pages_per_day // days

print(int(hours))
