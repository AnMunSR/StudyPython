# Bai tap lenh dieu khien co ban
'''
Bai19: Giai va bien luan phuong trinh ax^2 + bx + c = 0
'''

import math
a = int(input("Nhap vao so a: "))
b = int(input("Nhap vao so b: "))
c = int(input("Nhap vao so c: "))
if a == 0: 
    if c == 0:
        if b == 0:
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        if b == 0: 
            print("Phuong trinh vo nghiem")
        else:
            print("Nghiem cua phuong trinh la: ", -c/b)
else:
    denta = pow(b,2) - (4*a*c)
    if denta < 0:
        print("Phuong trinh vo nghiem")
    elif denta == 0:
        print("Phuong trinh co nghiem kep la: ", -b/(2*a))
    else:
        print("Nghiem x1 = ", (-b + math.sqrt(denta))/(2*a))
        print("Nghiem x2 = ", (-b - math.sqrt(denta))/(2*a))
