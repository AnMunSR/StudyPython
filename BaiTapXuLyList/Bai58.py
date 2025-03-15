# Bai tap xu ly list
# Bai 58:
''' 
Nhap vao mot list so nguyen L, nhap vao so nguyen x
tim gia tri trong list xa x nhat
'''

import math
# Ham khoang cach xa nhat
def timKhoangCachXaNhat(L, x):
    giaTriXaNhat = None
    khoangCachMax = -1
    for i in L:
        temp = abs(i - x)
        if temp > khoangCachMax:
            khoangCachMax = temp
            giaTriXaNhat = i
    return giaTriXaNhat


L = []
n = int(input("Nhap vao so luong phan tu cua L: n = "))

# Nhap cac phan tu trong list
for i in range(0,n):
    i = int(input("Nhap phan tu: "))
    L.append(i)
print("Danh sach L: ",L)

x = int(input("Nhap gia tri x: "))
print("Gia tri xa nhat so voi ",x,"la: ", timKhoangCachXaNhat(L, x))





