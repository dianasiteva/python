from datetime import date as datetype
from datetime import timedelta
from math import  floor

start_year = int(input())
end_year = int(input())
year_weight =int(input())

date = datetype(start_year, 1, 1)
found = False

while date.year <= end_year:
    d1 = floor(date.day / 10)
    d2 = date.day % 10
    d3 = floor(date.month / 10)
    d4 = date.month % 10
    d5 = floor(date.year / 1000)
    d6 = floor(date.year / 100) % 10
    d7 = floor(date.year / 10) % 10
    d8 = date.year % 10
    weight = d1 * (d2 + d3 + d4 + d5 + d6 + d7 + d8) + \
             d2 * (d3 + d4 + d5 + d6 + d7 + d8) + \
             d3 * (d4 + d5 + d6 + d7 + d8) + \
             d4 * (d5 + d6 + d7 + d8) + \
             d5 * (d6 + d7 + d8) + \
             d6 * (d7 + d8) + \
             d7 * d8
    if weight == year_weight:
        print(str(d1) + str(d2) + '-' + str(d3) + str(d4) + '-' + str(d5) + str(d6) + str(d7) + str(d8))
        found = True
    date = date + timedelta(days=1)

if not found:
    print('No')
