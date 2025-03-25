# Bai tap xay dung ham
# Bai 81:
'''
Viet ham dua vao 1 list so nguyen L va mot so nguyen duong a. Hay tim
va tra ve gia tri lon thu a trong list L (neu a = 1 thi tim gia tri lon
nhat, a= 2 thi tim gia tri lon thu 2. a = 3 thi tim gia tri lon thu ba,.)
'''

import math


# Ham sap xep danh sach giam dan
def sapXepGiamDan(l, n):
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]


# Ham tim gia tri lon thu a trong list l
def timGiaTriLonThuA(l, n, a):
    s = set()
    for i in range(0, n):
        s.add(l[i])
    list1 = list(s)
    sapXepGiamDan(list1, len(list1))
    return list1[a - 1]


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
print("Gia tri lon thu {0} trong day la {1}".format(a, timGiaTriLonThuA(l, n, a)))
