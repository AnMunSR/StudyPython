# Bai tap lenh dieu khien co ban
'''
Bai16: Tu bai so 15, neu a, b, c cau thanh duoc 1 tam giac, kiem tra
xem tam giac do la tam giac gi (can, deu, vuong, vuong can, thuong)
'''

import math
a = float(input("Nhap vao so a: "))
b = float(input("Nhap vao so b: "))
c = float(input("Nhap vao so c: "))
if a + b < c or a + c < b or b + c < a:
    print("Day khong phai la do dai 3 canh cua tham giac ")
else:
    print("Day  la do dai 3 canh cua tam giac")
    if a == b == c:
        print("Tam giac deu")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            if a == b or a == c or b == c:
                print("Tam giác vuông cân")
            else:
                print("Tam giác vuông")
    elif a == b or a == c or b == c:
       print("Tam giác cân")
    else:
        print("Tam giac thuong")
        