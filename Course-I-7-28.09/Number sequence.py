n = int(input())
max_number = 0
min_number = 0

for i in range(n):
    n_in = int(input())
    if i == 0:
        max_number = n_in
        min_number = n_in
    if n_in > max_number:
        max_number = n_in
    if n_in < min_number:
        min_number = n_in

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
