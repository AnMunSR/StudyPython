# Bai tap xay dung ham
# Bai 74:
'''
Viet ham dua vao 1 so nguyen a, kiem tra xem a co phai so nguyen to khong
'''

import math


# Ham kiem tra so nguyen to
def kiemTraSoNguyenTo(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


# Nhap du lieu dau vao
a = int(input("Nhap vao so nguyen a: "))
if kiemTraSoNguyenTo(a):
    print(a, "la so nguyen to!")
else:
    print(a, "khong phai so nguyen to!")
