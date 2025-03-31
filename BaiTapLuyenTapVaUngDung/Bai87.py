# Bai tap luyen tap va ung dung
# Bai 87:
'''
Viet ham cho gia tri dau vao la list so nguyen duong L va so nguyen
nguyen duong k. Hay tao va tra ve mot list L_kq co cac phan tu la
gia tri cua phan tu xuat hien nhieu hon k lan trong list L theo thu
tu tang dan
'''

import math


# Ham tra ve mot list co cac phan tu la gia tri cua phan tu xuat hien nhieu hon k lan va sap xep tang dan
def traVeList(L, n, k):
    L_kq = []
    s = set()
    for i in range(0, n):
        if L.count(L[i]) > k:
            s.add(L[i])
    L_kq = list(s)
    if len(L_kq) == 0:
        return "Khong ton tai"
    for i in range(0, len(L_kq) - 1):
        for j in range(i, len(L_kq)):
            if L_kq[i] > L_kq[j]:
                L_kq[i], L_kq[j] = L_kq[j], L_kq[i]
    return L_kq


# Nhap du lieu dau vao
L = []
n = int(input("Nhap so luong phan tu cua list L: "))
for i in range(0, n):
    i = int(input("Nhap gia tri cua list: "))
    L.append(i)
print("Danh sach ban dau: L = ", L)
k = int(input("Nhap vao so nguyen duong k: "))
print("Danh sach cac phan tu co so lan xuat hien nhieu hon ", k, "la: ", traVeList(L, n, k))
