# Bai tap lenh dieu khien co ban
'''
Bai17: Nhap vao 3 so a, b, c. Hay sap xep 3 so a, b, c theo thu tu tang dan 
roi in ra
'''

import math
a = int(input("Nhap vao so a: "))
b = int(input("Nhap vao so b: "))
c = int(input("Nhap vao so c: "))
if min(a,b,c) == a:
    print(a, end = " ")
    if min(b, c) == b:
        print(b, c)
    else:
        print(c, b)
elif min(a, b, c) == b:
    print(b, end = " ")
    if min(a, c) == a:
        print(a, c)
    else:
        print(c, a)
else:
    print(c, end = " ")
    if min(a, b) == a:
        print(a, b)
    else:
        print(b, a)