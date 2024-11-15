n = int(input())

n_out = ''
n_middle = str(n)

for j in range(0, len(str(n))):
    n_in = n_middle
    n_middle = ''
    max_n = n_in[0]
    ii = 0
    for i in range(0, len(n_in)):
        if int(n_in[i]) > int(max_n):
            max_n = n_in[i]
            ii = i
    for jj in range(0, len(n_in)):
        if jj != ii:
            n_middle += n_in[jj]
    n_out += max_n

print(n_out)
