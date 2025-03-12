# Bai toan nhap lieu va toan tu co ban:
'''
Bai6: Nhap vao so nguyen a, neu a la so chia het cho 5 nhung
khong nam trong khoanf tu 20 - 70 thi in ra True, nguoc lai in ra False
'''

import math
a = int(input("Nhap vao so nguyen a: "))
if a % 5 != 0 and a <= 70 and a >= 20:
    print("False")
else:
    print("True")