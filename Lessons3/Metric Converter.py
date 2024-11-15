size = float(input())
in_m = input().lower()
out_m = input().lower()

m = 1
mm = 1000
cm = 100
mi = 0.000621371192
inch = 39.3700787
km = 0.001
ft = 3.2808399
yd = 1.0936133

dest = size
if in_m == 'm':
    dest /= m
if in_m == 'mm':
    dest /= mm
if in_m == 'mi':
    dest /= mi
if in_m == 'cm':
    dest /= cm
if in_m == 'in':
    dest /= inch
if in_m == 'km':
    dest /= km
if in_m == 'ft':
    dest /= ft
if in_m == 'yd':
    dest /= yd

if out_m == 'm':
    dest *= m
if out_m == 'mm':
    dest *= mm
if out_m == 'mi':
    dest *= mi
if out_m == 'cm':
    dest *= cm
if out_m == 'in':
    dest *= inch
if out_m == 'km':
    dest *= km
if out_m == 'ft':
    dest *= ft
if out_m == 'yd':
    dest *= yd

print(f'{size} {dest}')
