# Bai tap xay dung ham
# Bai 79:
'''
Viet ham dua vao mot list so nguyen L va 1 so nguyen duong a. Hay tinh
va tra ve gia tri trung binh cua a phan tu dau tien trong L
'''

import math


# Ham tinh gia tri trung binh cua a phan tu dau tien trong l
def tinhGiaTriTBCuaAPhanTuDauTien(l, n, a):
    tb = 0
    if a <= n:
        for i in range(0, a):
            tb += l[i]
        tb /= a
    elif a > n:
        for i in range(0, n):
            tb += l[i]
        tb /= n
    return tb


# Nhap du lieu dau vao
n = int(input("Nhap so luong phan tu cua list: "))
l = []
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    l.append(i)
while True:
    a = int(input("Nhap vao gia tri cua a: "))
    if a > 0:
        break
print("Gia tri trung binh cua a so dau tien trong list l: ", tinhGiaTriTBCuaAPhanTuDauTien(l, n, a))
