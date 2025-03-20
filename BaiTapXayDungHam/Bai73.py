# Bai tap xay dung ham
# Bai 73:
'''
Viet ham dua vao 2 so nguyen, so nao lon hon thi in ra ban cuu chuong
'''

import math


# Ham in ra bang cuu chuong
def inBangCuuChuong(a, b):
    if a > b:
        for i in range(1, 11):
            print(a, "x", i, "=", a * i)
    else:
        for i in range(1, 11):
            print(b, "x", i, "=", b * i)


# Nhap du lieu dau vao
a = int(input("Nhap vao so nguyen a: "))
b = int(input("Nhap vao so nguyen b: "))
inBangCuuChuong(a, b)
