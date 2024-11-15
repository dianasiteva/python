n = int(input())

OddSum = 0
EvenSum = 0
OddMin = 'No'
OddMax = 'No'
EvenMin = 'No'
EvenMax = 'No'

if n != 0:
    for i in range(1, n + 1):
        num = float(input())
        if i % 2 == 0:
            EvenSum += num
            if EvenMax == 'No':
                EvenMax = num
                EvenMin = num
            else:
                if num > EvenMax:
                    EvenMax = num
                elif num < EvenMin:
                    EvenMin = num
        else:
            OddSum += num
            if OddMax == 'No':
                OddMax = num
                OddMin = num
            else:
                if num > OddMax:
                    OddMax = num
                elif num < OddMin:
                    OddMin = num

if OddSum != int(OddSum):
    print('OddSum=' + str(OddSum) + ',')
else:
    print('OddSum=' + str(int(OddSum)) + ',')

if type(OddMin) == str:
    print('OddMin=No,')
else:
    if OddMin != int(OddMin):
        print('OddMin=' + str(OddMin) + ',')
    else:
        print('OddMin=' + str(int(OddMin)) + ',')

if type(OddMax) == str:
    print('OddMax=No,')
else:
    if OddMax != int(OddMax):
        print('OddMax=' + str(OddMax) + ',')
    else:
        print('OddMax=' + str(int(OddMax)) + ',')

if EvenSum != int(EvenSum):
    print('EvenSum=' + str(EvenSum) + ',')
else:
    print('EvenSum=' + str(int(EvenSum)) + ',')

if type(EvenMin) == str:
    print('EvenMin=No,')
else:
    if EvenMin != int(EvenMin):
        print('EvenMin=' + str(EvenMin) + ',')
    else:
        print('EvenMin=' + str(int(EvenMin)) + ',')

if type(EvenMax) == str:
    print('EvenMax=No')
else:
    if EvenMax != int(EvenMax):
        print('EvenMax=' + str(EvenMax))
    else:
        print('EvenMax=' + str(int(EvenMax)))
