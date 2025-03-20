# Bai tap xu ly list
# Bai 68:
'''
Nhap vao mot list so nguyen L, hay bien doi L bang cach thay doi vi tri giua gia
tri nho nhat va lon nhat
'''

import math


# Ham tim vi tri gia tri nho nhat list
def minList(L, n):
    temp = L[0]
    pos = 0
    for i in range(1, n):
        if L[i] < temp:
            temp = L[i]
            pos = i
    return pos


# Ham tim vi tri gia tri lon nhat cua list
def maxList(L, n):
    temp = L[0]
    pos = 0
    for i in range(1, n):
        if L[i] > temp:
            temp = L[i]
            pos = i
    return pos


# Nhap du lieu dau vao
n = int(input("Nhap vao so luong phan tu cua list L: "))
L = []
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    L.append(i)

print("Danh sach L: ", L)
a = minList(L, n)
b = maxList(L, n)
L[a], L[b] = L[b], L[a]
print("Dach sau sau khi hoan doi vi tri lon nhat va nho nhat: ", L)
