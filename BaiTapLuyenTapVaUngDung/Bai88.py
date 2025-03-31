# Bai tap luyen tap va ung dung
# Bai 88:
'''
Viet ham cho gia tri dau vao la list so nguyen duong L va so nguyen
duong k. Tim va tra ve doan list dai nhat trong L co gia tri trung binh
la k
'''

import math


# Ham tra ve doan list dai nhat trong L co gia tri trung binh la k
def timDoanDaiNhat(L, n, k):
    max_len = 0
    L_kq = []
    for i in range(0, n):
        for j in range(i, n):
            subList = L[i:j + 1]
            if sum(subList) / len(subList) == k:
                if len(subList) > max_len:
                    max_len = len(subList)
                    L_kq = subList
    return L_kq


# Nhap du lieu dau vao
L = []
n = int(input("Nhap so luong phan tu cua list L: "))
for i in range(0, n):
    i = int(input("Nhap gia tri: "))
    L.append(i)
print("Danh sach ban dau: ", L)
k = int(input("Nhap vao gia tri k: "))
print("Doan list dai nhat co gia tri trung binh = ", k, "la: ", timDoanDaiNhat(L, n, k))
