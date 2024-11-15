import math

money = float(input())
floor_width = float(input())
floor_height = float(input())
tile_a = float(input())
tile_h = float(input())
price_per_tile = float(input())
master_price = float(input())

floor = floor_height *  floor_width
tile = tile_a * tile_h / 2
tile_number = math.ceil(floor / tile) + 5

price = tile_number * price_per_tile + master_price
diff = abs(price - money)
if price <= money:
    print(f"{diff:.2f} lv left.")
else:
    print(f"You'll need {diff:.2f} lv more.")