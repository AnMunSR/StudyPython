# Bai toan nhap lieu va toan tu co ban:
'''
Bai12: Nhap vao 3 so a, b, c. Tinh va in ra d = (a + b)^c
Neu d la so trong khoang tu 100 - 200 thi in ra True, nguoc lai in ra False
'''

import math
a = float(input("Nhap vao so a: "))
b = float(input("Nhap vao so b: "))
c = float(input("Nhap vao so c: "))
d = pow(a+b,c)
if d >= 100 and d <= 200: 
    print("True")
else:
    print("False")