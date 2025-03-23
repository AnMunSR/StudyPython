# Bai tap xay dung ham
# Bai 78:
'''
Viet ham dua vao mot list co cac phan tu la chuoi, tim va tra ve chuoi
ngan nhat trong list
'''

import math


# Ham tim va tra ve chuoi ngan nhat
def timChuoiNganNhat(l, n):
    chuoiMin = l[0]
    lenMin = len(l[0])
    for i in range(1, n):
        if len(l[i]) < lenMin:
            chuoiMin = l[i]
            lenMin = len(l[i])
    return chuoiMin, lenMin


# Nhap du lieu dau vao
n = int(input("Nhap so luong phan tu cua list: "))
l = []
for i in range(0, n):
    i = input("Nhap phan tu: ")
    l.append(i)
print("Chuoi ngan nhat va do dai cua no la: ", timChuoiNganNhat(l, n))
