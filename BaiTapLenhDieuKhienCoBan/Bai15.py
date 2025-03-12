# Bai tap lenh dieu khien co ban
'''
Bai15: Nhap vao 3 so thuc duong a, b, c. Kiem tra xem a, b, c co
cau thanh do dai cua 1 tam giac duoc khong
'''

import math
a = float(input("Nhap vao so a: "))
b = float(input("Nhap vao so b: "))
c = float(input("Nhap vao so c: "))
if a + b < c or a + c < b or b + c < a:
    print("Day khong phai la do dai 3 canh cua tham giac ")
else:
    print("Day  la do dai 3 canh cua tam giac")