in_string = input().lower()
j = 0
l_in_string = len(in_string)
l_sun = 3
l_sand = 4
l_fish = 4
l_water = 5

for i in range(0, len(in_string)):
    if i + l_sun <= l_in_string:
        if in_string[i:i + l_sun] == 'sun':
            j += 1
    if i + l_sand <= l_in_string:
        if in_string[i:i + l_sand] == 'sand':
            j += 1
    if i + l_fish <= l_in_string:
        if in_string[i:i + l_fish] == 'fish':
            j += 1
    if i + l_water <= l_in_string:
    #    print(in_string[i:l_water])
        if in_string[i:i + l_water] == 'water':
            j += 1

print(j)

