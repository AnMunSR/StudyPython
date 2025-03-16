# Bai tap xu ly list
# Bai 63:
''' 
Nhap vao mot list so nguyen L. Hay tim va in ra vi 
tri trong L thoa man 2 dieu kien: co 2 gia tri lan
can va gia tri tai vi tri do bang tich 2 gia tri 
lan can. Neu L khong ton tai gia tri nhu vay thi in
ra -1
'''

import math

# Ham xac dinh vi tri
def timViTri(L):
    for i in range(1, len(L) - 1):
        if L[i] == L[i - 1] * L[i + 1]:
            return i
    return -1 

# Nhap du lieu dau vao
L = []
n = int(input("Nhap so phan tu cua list: n = "))
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    L.append(i)

print("Danh sach list: ",L)

print("Vi tri: ", timViTri(L))
