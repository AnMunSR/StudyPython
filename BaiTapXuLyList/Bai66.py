# Bai tap xu ly list
# Bai 66:
''' 
Nhap vao mot list so nguyen L, hay dem so luong gia tri 
trong list thoa tinh chat: "lon hon tat ca cac gia tri
dung dang truoc no"
'''

import math

# Ham kiem tra phan tu lon hon tat ca cac phan tu truoc no
def kiemTraLonHon(L):
    count = 1
    max_truoc = L[0]
    for i in range(1, len(L)):
        if L[i] > max_truoc:
            count += 1
            max_truoc = L[i]
    return count

# Nhap du lieu dau vao
L = []
n = int(input("Nhap so phan tu cua list: n = "))
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    L.append(i)

print("Danh sach list: ",L)
print("So phan tu thoa man dieu kien la: ", kiemTraLonHon(L))


