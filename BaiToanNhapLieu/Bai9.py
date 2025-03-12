# Bai toan nhap lieu va toan tu co ban:
'''
Bai9: Nhap vao so nguyen a, kiem tra xem a co phai so chinh 
phuong hay khong, neu co in ra True, nguoc lai in ra False
'''

import math
a = int(input("Nhap vao so nguyen a: "))
b = math.sqrt(a)
if int(b) == b:
    print("True")
else:
    print("False")