# Bai tap xay dung ham
# Bai 76:
'''
Viet ham dua vao mot list so nguyen, tim va tra ve vi tri co gia tri lon nhat
trong list
'''

import math


# Ham tim va tra vi vi tri co gia tri lon nhat
def timViTriLonNhat(l, n):
    pos = 0
    lmx = []
    maxTemp = l[0]
    for i in range(1, n):
        if l[i] > maxTemp:
            maxTemp = l[i]
            pos = i
    for i in range(0, n):
        if l[i] == maxTemp:
            lmx.append(i)
    return lmx


# Nhap du lieu dau vao
n = int(input("Nhap so luong phan tu cua list: "))
l = []
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    l.append(i)
print("Vi tri phan tu lon nhat torng list: ", timViTriLonNhat(l, n))
