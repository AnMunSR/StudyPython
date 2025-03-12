# Bai tap lenh dieu khien co ban
'''
Bai18: Giai va bien luan phuong trinh ax + b = 0
'''

import math
a = int(input("Nhap vao so a: "))
b = int(input("Nhap vao so b: "))
if b == 0:
    if a == 0:
        print("Phuong trinh co vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    if a == 0: 
        print("Phuong trinh vo nghiem")
    else:
        print("Nghiem cua phuong trinh la: ", -b/a)