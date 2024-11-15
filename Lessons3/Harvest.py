import math

vineyard_area = int(input())
grape_per_square = float(input())
needed_liters = int(input())
workers = int(input())

harvest_per_vine = vineyard_area * grape_per_square * 0.4
vine = harvest_per_vine / 2.5

if needed_liters <= vine:
    vine_left = math.ceil(vine - needed_liters)
    per_br = math.ceil(vine_left / workers)
    print(f'Good harvest this year! Total wine: {math.floor(vine)} liters.\n{vine_left} liters left -> {per_br} liters per person.')
else:
    to_br = math.floor(needed_liters - vine)
    print(f'It will be a tough winter! More {to_br} liters wine needed.')