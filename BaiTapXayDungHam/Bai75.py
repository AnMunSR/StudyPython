# Bai tap xay dung ham
# Bai 75:
'''
Viet ham dua vao mot so nguyen a, kiem tra xem a co phai la so Armstrong hay khong
'''

import math


# Ham kiem tra so Armstrong
def kiemTraSoArmstrong(a):
    chuoi = str(a) # Chuyen so thanh chuoi
    doDai = len(chuoi)
    tong = 0
    for i in range(0,doDai):
        tong += math.pow(int(chuoi[i]),doDai)
    if tong != a:
        return False
    return True


# Nhap du lieu dau vao
a = int(input("Nhap vao so nguyen a: "))
if kiemTraSoArmstrong(a):
    print(a, "la so Armstrong!")
else:
    print(a, "khong phai so Armstrong")