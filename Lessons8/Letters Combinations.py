start_letter = input().lower()
stop_letter = input().lower()
except_letter = ord(input().lower())

s = ''
n = 0

for i in range(ord(start_letter), ord(stop_letter) + 1):
    if except_letter != i:
        for j in range(ord(start_letter), ord(stop_letter) + 1):
            if except_letter != j:
                for k in range(ord(start_letter), ord(stop_letter) + 1):
                    if except_letter != k:
                        s += chr(i) + chr(j) + chr(k) + ' '
                        n += 1

print(s + str(n))
