# Bai tap xu ly list
# Bai 69:
'''
Nhap vao mot list L co cac phan tu bao gom chuoi va so nguyen, hay tim va in ra
chuoi co do dai lon nhat va so nguyen co gia tri nho nhat
'''

import math


# Ham tim gia tri nho nhat list
def minList(L, n):
    temp = L[0]
    for i in range(1, n):
        if L[i] < temp:
            temp = L[i]
    return temp


# Ham tim chuoi co do dai dai nhat trong list
def timChuoiCoDoDaiMax(L, n):
    temp = len(L[0])
    chuoi = L[0]
    for i in range(1, n):
        if len(L[i]) > temp:
            temp = len(L[i])
            chuoi = L[i]
    return chuoi


# Nhap du lieu dau vao
n = int(input("Nhap vao so luong phan tu cua list L: "))
L = []
for i in range(0, n):
    i = input("Nhap vao phan tu: ")
    L.append(i)

print("Danh sach L: ", L)

# Chia list thanh 2 list chuoi va so nguyen
L1 = []  # list so nguyen
L2 = []  # list chuoi
for i in range(0, n):
    if L[i].isdigit():
        L1.append(int(L[i]))
    else:
        L2.append(L[i])

print("So nguyen nho nhat trong list: ", minList(L1, len(L1)))
print("Chuoi dai nhat trong list: ", timChuoiCoDoDaiMax(L2, len(L2)))
