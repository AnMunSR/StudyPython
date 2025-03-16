# Bai tap xu ly list
# Bai 61:
''' 
Nhap vao mot list so nguyen L, hay sap xep L tang dan
'''

import math

# Ham sap xep list tang dan
def sapXepTangDan(L):
    for i in range(0, len(L) - 1):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]

# Nhap du lieu dau vao
L = []
n = int(input("Nhap so phan tu cua list: n = "))
for i in range(0, n):
    i = int(input("Nhap phan tu: "))
    L.append(i)

print("Danh sach list: ",L)
sapXepTangDan(L)
print("Danh sach sau khi sap xep tang dan: ", L)



