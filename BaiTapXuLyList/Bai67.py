# Bai tap xu ly list
# Bai 67:
''' 
Nhap vao mot list so nguyen L, hay dua cac so chan 
trong list ve dau list, so le ve cuoi list va cac 
phan tu 0 nam giua
'''

import math

# Ham chia chan le
def chiaChanLe(L):
    Lchan = [x for x in L if x % 2 == 0 and x != 0]
    Lle = [x for x in L if x % 2 != 0] 
    Lkhong = [x for x in L if x == 0] 
    return Lchan + Lkhong + Lle

# Nhap du lieu dau vao
L = []
n = int(input("Nhap so phan tu cua list: n = "))
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    L.append(i)

print("Danh sach list: ",L)
print("Danh sach da sap xep chan le: ", chiaChanLe(L))


