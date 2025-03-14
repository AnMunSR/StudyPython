# Bai tap vong lap while
# Bai 40: Nhap vao so nguyen duong n, tinh tong cac chu so cua n


import math
from datetime import datetime

# Ham dem so luong chu so chan, le trong n
def tinhTong(n):
    tong = 0 
    while n > 0:
        temp = n % 10
        tong += temp
        n //= 10
    return tong

# Nhap du lieu dau vao
n = int(input("Nhap vao so n = "))
print("Tinh tong cac chu so trong ", n, " la: ", tinhTong(n))
