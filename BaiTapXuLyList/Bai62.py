# Bai tap xu ly list
# Bai 62:
''' 
Nhap vao mot list so nguyen L, hay kiem tra xem L co
phai la mot cap so cong hay khong? Neu co thi tim va
in ra cong sai, neu khong co thi in ra None
'''

import math

# Ham kiem tra cap so cong
def kiemTraCapSoCong(L):
    if len(L) < 2:
        return True
    d = L[1] - L[0]
    for i in range(1, len(L) - 1):
        if L[i+1] - L[i] != d:
            return False
    return True

# Nhap du lieu dau vao
L = []
n = int(input("Nhap so phan tu cua list: n = "))
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    L.append(i)

print("Danh sach list: ",L)
if kiemTraCapSoCong(L):
    print("L la cap so cong!")
    print("Cong sai d = ", L[1] - L[0])
else:
    print("L khong phai cong sai!")



