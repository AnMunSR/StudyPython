# Bai tap xu ly list
# Bai 60:
''' 
Nhap vao mot list so nguyen L, hay kiem tra xem L co
duoc sap xep tu be den lon hay khong. Neu co in True,
neu khong in False
'''

import math

# Ham kiem tra list co tang dan khong
def kiemTraTangDan(L):
    for i in range(0,len(L) - 1):
        if L[i] > L[i+1]:
            return False
    return True

# Nhap du lieu dau vao
L = []
n = int(input("Nhap so phan tu cua list: n = "))
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    L.append(i)

print("Danh sach list: ",L)

if kiemTraTangDan(L):
    print("True")
else:
    print("False")




