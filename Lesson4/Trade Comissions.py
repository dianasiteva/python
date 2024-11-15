town = input().lower()
sales = float(input())

comission = -1

if town == 'sofia':
    if 0 <= sales <= 500:
        comission = 0.05
    elif 500 < sales <= 1000:
        comission = 0.07
    elif 1000 < sales <= 10000:
        comission = 0.08
    elif sales > 10000:
        comission = 0.12
elif town == 'plovdiv':
    if 0 <= sales <= 500:
        comission = 0.055
    elif 500 < sales <= 1000:
        comission = 0.08
    elif 1000 < sales <= 10000:
        comission = 0.12
    elif sales > 10000:
        comission = 0.145
elif town == 'varna':
    if 0 <= sales <= 500:
        comission = 0.045
    elif 500 < sales <= 1000:
        comission = 0.075
    elif 1000 < sales <= 10000:
        comission = 0.1
    elif sales > 10000:
        comission = 0.13

if comission > 0:
    print('%.2f' % (sales * comission))
else:
    print('error')