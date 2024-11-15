days = int(input())
total_liters = 0
total_degree = 0

for i in range(1, days + 1):
    liters = float(input())
    degree = float(input())
    total_liters += liters
    total_degree += degree * liters

end_degree = total_degree / total_liters

print(f'Liter: {total_liters:.2f}')
print(f'Degrees: {end_degree:.2f}')
if end_degree < 38:
    print('Not good, you should baking!')
elif end_degree > 42:
    print('Dilution with distilled water!')
else:
    print('Super!')
