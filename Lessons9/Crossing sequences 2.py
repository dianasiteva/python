tribonacci1 = int(input())
tribonacci2 = int(input())
tribonacci3 = int(input())
spiral_current = int(input())
spiral_step = int(input())

tribonacci_current = tribonacci1
count = 0
spiral_count = 0
spiral_current_mul = 1
found = False

while tribonacci_current <= 1000000 and spiral_current <= 1000000:
    if tribonacci_current == spiral_current:
        print(tribonacci_current)
        found = True
        break
    elif tribonacci_current < spiral_current:
        if count > 2:
            tribonacci_current = tribonacci1 + tribonacci2 + tribonacci3
            tribonacci1 = tribonacci2
            tribonacci2 = tribonacci3
            tribonacci3 = tribonacci_current
        elif count == 0:
            tribonacci_current = tribonacci2
            count += 1
        elif count == 1:
            tribonacci_current = tribonacci2
            count += 1
        elif count == 2:
            tribonacci_current = tribonacci3
            count += 1
    else:
        spiral_current += spiral_step * spiral_current_mul
        spiral_count += 1
        if spiral_count % 2 == 0:
            spiral_current_mul += 1

if not found:
    print('No')
