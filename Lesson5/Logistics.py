count_of_loads = int(input())
tons = 0
microbus_tons = 0
truck_tons = 0
train_tons = 0
sum_tons = 0
total_price = 0

for i in range(0, count_of_loads):
    tons = int(input())
    sum_tons += tons
    if tons <= 3:
        microbus_tons += tons
    elif 3 < tons <= 11:
        truck_tons += tons
    elif tons > 11:
        train_tons += tons

total_price = microbus_tons * 200 + truck_tons * 175 + train_tons * 120

print('%.2f' % (total_price / sum_tons))
print('%.2f' % (microbus_tons * 100 / sum_tons) + '%')
print('%.2f' % (truck_tons * 100 / sum_tons) + '%')
print('%.2f' % (train_tons * 100 / sum_tons) + '%')
