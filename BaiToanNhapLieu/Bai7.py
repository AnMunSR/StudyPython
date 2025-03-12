# Bai toan nhap lieu va toan tu co ban:
'''
Bai7: Nhap vao so nguyen a va b, neu 1 trong 2 so a va b chia het cho 2 
thi in ra True, nguoc lai in ra False
'''

import math
a = int(input("Nhap vao so nguyen a: "))
b = int(input("Nhap vao so nguyen b: "))
if a % 2 == 0 or b % 2 == 0:
    print("True")
else:
    print("False")