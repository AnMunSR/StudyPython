# Bai tap xu ly list
# Bai 65:
''' 
Nguoi ta dinh nghia mot list do nguyen duoc goi la "dang
song" khi tat ca cac phan tu deu lon hon hoac nho hon 2 
phan tu xung quanh no.
Nhap vao mot list so nguyen L va kiem tra L co phai list
dang song hay khong, neu co in ra True, khong in ra False
'''

import math

# Ham kiem tra dang song
def kiemTraDangSong(L):
    for i in range(1, len(L) - 1):
        if ((L[i] >= L[i+1]) and (L[i] <= L[i-1])) or ((L[i] <= L[i+1]) and (L[i] >= L[i-1])):
            return False
    return True

# Nhap du lieu dau vao
L = []
n = int(input("Nhap so phan tu cua list: n = "))
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    L.append(i)

print("Danh sach list: ",L)
if kiemTraDangSong(L):
    print("L co dang song!")
else:
    print("L khong phai dang song!")



