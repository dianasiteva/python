tribonacci1 = int(input())
tribonacci2 = int(input())
tribonacci3 = int(input())
spiral_current = int(input())
spiral_step =int(input())

tribonacci_numbers = [tribonacci1, tribonacci2, tribonacci3]
tribonacci_current = tribonacci3

while tribonacci_current < 1000000:
    tribonacci_current = tribonacci1 + tribonacci2 + tribonacci3
    tribonacci_numbers.append(tribonacci_current)
    tribonacci1 = tribonacci2
    tribonacci2 = tribonacci3
    tribonacci3 = tribonacci_current

spiral_count = 0
spiral_current_mul = 1
spiral_numbers = [spiral_current]

while spiral_current < 1000000:
    spiral_current += spiral_step * spiral_current_mul
    spiral_numbers.append(spiral_current)
    spiral_count += 1
    if spiral_count % 2 == 0:
        spiral_current_mul += 1

found = False

for i in range(0, len(tribonacci_numbers)):
    for j in range(0, len(spiral_numbers)):
        if tribonacci_numbers[i] == spiral_numbers[j] and tribonacci_numbers[i] <= 1000000:
            print(tribonacci_numbers[i])
            found = True
            break
    if found:
        break

if not found:
    print('No')