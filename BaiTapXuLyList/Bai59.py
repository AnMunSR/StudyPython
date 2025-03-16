# Bai tap xu ly list
# Bai 59:
''' 
Nhap vao mot list so nguyen L, tinh gia tri trung binh cua list L
'''

import math


# Nhap du lieu dau vao
L = []
n = int(input("Nhap so phan tu cua list: n = "))
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    L.append(i)

# Tinh gia tri trung binh cua list
tb = 0
for i in L:
    tb += i
tb = tb / n
print("Gia tri trung binh cua list: ", tb)




