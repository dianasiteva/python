print("Enter two integers: ")
num1 = int(input())
num2 = int(input())

if num1 > num2:
    print("Greater number: " + str(num1))
else:
    print("Greater number: " + str(num2))

fir = int(input())
sec = int(input())
res = 0
if fir > sec:
    res = fir - sec
    print(res)
elif sec > fir:
    res = sec - fir
    print(res)
elif sec == fir:
    print(res)
