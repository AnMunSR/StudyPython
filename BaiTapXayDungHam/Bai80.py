# Bai tap xay dung ham
# Bai 80:
'''
Viet ham dua vao mot list so nguyen L va 1 so nguyen duong a. Hay tim
va tra ve mot list moi co so phan tu la a , gia tri cac phan tu la cac
so nguyen to tim duoc trong list L
'''

import math


# Ham kiem tra so nguyen to
def kiemTraSoNguyenTo(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Ham tim va tra ve list co a phan tu, cac phan tu la so nguyen to tim duoc trong list l
def timDanhSachSoNguyenTo(l, n, a):
    result = []
    for i in range(0, n):
        if kiemTraSoNguyenTo(l[i]):
            if len(result) < a:
                result.append(l[i])
            else:
                return result
    return result


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
print("Danh sach chua a phan tu la so nguyen to trong list l: ", timDanhSachSoNguyenTo(l, n, a))
