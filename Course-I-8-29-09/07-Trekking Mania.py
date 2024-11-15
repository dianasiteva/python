n_groups = int(input())
numbers_in_groups = 0
pr_musala = 0
pr_montblan = 0
pr_kilimanjaro = 0
pr_k2 = 0
pr_everest = 0

for i in range(n_groups):
    n_in_gr = int(input())
    numbers_in_groups += n_in_gr

    if n_in_gr <= 5:
        pr_musala += n_in_gr
    elif 6 <= n_in_gr <= 12:
        pr_montblan += n_in_gr
    elif 13 <= n_in_gr <= 25:
        pr_kilimanjaro += n_in_gr
    elif 26 <= n_in_gr <= 40:
        pr_k2 += n_in_gr
    elif n_in_gr > 40:
        pr_everest += n_in_gr

print(f'{pr_musala * 100 / numbers_in_groups:.2f}%')
print(f'{pr_montblan * 100 / numbers_in_groups:.2f}%')
print(f'{pr_kilimanjaro * 100 / numbers_in_groups:.2f}%')
print(f'{pr_k2 * 100 / numbers_in_groups:.2f}%')
print(f'{pr_everest * 100 / numbers_in_groups:.2f}%')
