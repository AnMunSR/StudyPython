# Bai tap xay dung ham
# Bai 77:
'''
Viet ham dua vao mot list so nguyen va mot so nguyen duong k. Hay tim va
tra ve vi tri cua phan tu dau tien co gia tri k trong list so nguyen,
neu khong co thi tra ve -1
'''

import math


# Ham tim va tra ve vi tri cua k
def timViTriK(l, n, k):
    pos = -1
    for i in range(0, n):
        if (l[i] == k):
            pos = i
            return pos
    return pos


# Nhap du lieu dau vao
n = int(input("Nhap so luong phan tu cua list: "))
l = []
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    l.append(i)

k = int(input("Nhap vao k: "))
if (timViTriK(l, n, k) == -1):
    print("Khong tim thay phan tu k trong list l!")
else:
    print("Vi tri xuat hien dau tien cua k trong list la: ", timViTriK(l, n, k))
