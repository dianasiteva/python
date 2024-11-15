n = int(input())
n0 = 0
n1 = 0
s0 = ""
s1 = ""

if n == 0:
    s0 = "zero"
if n == 1:
    s0 = "one"
if n == 2:
    s0 = "two"
if n == 3:
    s0 = "three"
if n == 4:
    s0 = "four"
if n == 5:
    s0 = "five"
if n == 6:
    s0 = "six"
if n == 7:
    s0 = "seven"
if n == 8:
    s0 = "eight"
if n == 9:
    s0 = "nine"
if n == 10:
    s0 = "ten"

if 10 < n < 100:
    n0 = n % 10
    n1 = n // 10

if n0 == 1 and n1 != 1:
    s0 = "one"
if n0 == 1 and n1 == 1:
    s0 = "eleven"
if n0 == 2 and n1 != 1:
    s0 = "two"
if n0 == 2 and n1 == 1:
    s0 = "twelve"
if n0 == 3 and n1 != 1:
    s0 = "three"
if n0 == 3 and n1 == 1:
    s0 = "thirteen"
if n0 == 4 and n1 != 1:
    s0 = "four"
if n0 == 4 and n1 == 1:
    s0 = "fourteen"
if n0 == 5 and n1 != 1:
    s0 = "five"
if n0 == 5 and n1 == 1:
    s0 = "fifteen"
if n0 == 6 and n1 != 1:
    s0 = "six"
if n0 == 6 and n1 == 1:
    s0 = "sixteen"
if n0 == 7 and n1 != 1:
    s0 = "seven"
if n0 == 7 and n1 == 1:
    s0 = "seventeen"
if n0 == 8 and n1 != 1:
    s0 = "eight"
if n0 == 8 and n1 == 1:
    s0 = "eighteen"
if n0 == 9 and n1 != 1:
    s0 = "nine"
if n0 == 9 and n1 == 1:
    s0 = "nineteen"

if n1 == 2:
    s1 = "twenty"
if n1 == 3:
    s1 = "thirty"
if n1 == 4:
    s1 = "forty"
if n1 == 5:
    s1 = "fifty"
if n1 == 6:
    s1 = "sixty"
if n1 == 7:
    s1 = "seventy"
if n1 == 8:
    s1 = "eighty"
if n1 == 9:
    s1 = "ninety"

if n < 20:
    print(s0)

if 100 > n > 19:
    if n0 == 0:
        print(s1)
    else:
        print(s1 + " " + s0)

if n == 100:
    print("one hundred")
