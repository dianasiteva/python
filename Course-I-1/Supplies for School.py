PEN_PACKET_PRICE = 5.80
MARKER_PACKET_PRICE = 7.20
CLEANER = 1.20

pen_packets_number = int(input())
marker_packets_number = int(input())
cleaner_litres = int(input())
discount_percent = int(input()) / 100

total_price = (pen_packets_number * PEN_PACKET_PRICE
               + MARKER_PACKET_PRICE * marker_packets_number + cleaner_litres * CLEANER)
discount_sum = total_price * discount_percent
price = total_price - discount_sum

print(price)
