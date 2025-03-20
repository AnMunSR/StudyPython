# Bai tap xu ly list
# Bai 71:
'''
Nhap vao mot list L co cac phan tu la chuoi (khong chua ku tu dac biet, dau cau,
ki tu so, chi co ki tu chu cai va khoang trang)
Hay tim vi tri cua chuoi co nhieu tu nhat
'''

import math


# Ham tim vi tri cua chuoi co nhieu tu nhat
def viTriChuoiCoNhieuTuNhat(L, n):
    pos = 0
    result = L[0].split()
    temp = len(result)
    for i in range(1, n):
        result = L[i].split()
        if temp < len(result):
            temp = len(result)
            pos = i
    return pos


# Nhap du lieu dau vao
L = []
n = int(input("Nhap so luong phan tu cua L: "))
for i in range(0, n):
    i = input("Nhap phan tu: ")
    L.append(i)
print("Danh sach list L: ", L)
print("Vi tri cua chuoi co nhieu tu nhat trong L: ", viTriChuoiCoNhieuTuNhat(L, n))
