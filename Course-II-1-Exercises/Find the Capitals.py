in_str = input()
out_str = []

for i in range(0, len(in_str)):
    if in_str[i].isupper():
        out_str.append(i)

print(out_str)